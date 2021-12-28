from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template, request, redirect, session, send_file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from flask_session import Session
import pandas as pd
from googlesearch import search
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

deptDict = {
	'Aerospace Engineering': {
		'list': ['https://www.aero.iitb.ac.in/home/people/faculty','https://www.aero.iitb.ac.in/home/people/former-faculty'],
		'query': 'iit Aerospace Engineer faculty name',
		},
    'Biosciences and Bioengineering':{
    	'list':['https://www.bio.iitb.ac.in/people/faculty/'],
    	'query': 'iit Biosciences and Bioengineer faculty name',
    	},
    'Chemical Engineering':{
    	'list':['https://www.che.iitb.ac.in/faculty-directory'],
    	'query': 'iit Chemical Engineer faculty name',
    	},
    'Chemistry':{ 
    	'list':[],
    	'query': ''
    },
    'Civil Engineering':{ 
    	'list':['https://www.civil.iitb.ac.in/faculty'],
    	'query': 'iit Civil Engineer faculty name'
    },
    'Computer Science & Engineering':{ 
    	'list':[],
    	'query': ''
    },
    'Earth Sciences':{ 
    	'list':[],
    	'query': ''
    },
    'Electrical Engineering':{ 
    	'list':[],
    	'query': ''
    },
    'Energy Science and Engineering':{ 
    	'list':['https://www.me.iitb.ac.in/?q=full-time-faculty'],
    	'query': 'iit Energy Science Engineer faculty name'
    },
    'Environmental Science and Engineering (ESED)':{ 
    	'list':['http://www.esed.iitb.ac.in/faculty-directory'],
    	'query': 'iit Environmental Science Engineer faculty name'
    },
    'Humanities & Social Sciences':{ 
    	'list':[],
    	'query': ''
    },
    'Mathematics':{ 
    	'list':[],
    	'query': ''
    },
    'Mechanical Engineering':{ 
    	'list':['http://www.esed.iitb.ac.in/faculty-directory','https://www.me.iitb.ac.in/?q=honorary-faculty-members'],
    	'query': 'iit Mechanical Engineer faculty name'
    },
    'Metallurgical Engineering & Materials Science':{ 
    	'list':[],
    	'query': ''
    },
    'Physics':{ 
    	'list':['https://www.phy.iitb.ac.in/en/faculty'],
    	'query': 'iit Physics Engineer faculty name'
    },
    'All': { 
    	'list':[
     	'https://www.aero.iitb.ac.in/home/people/faculty',
     	'https://www.aero.iitb.ac.in/home/people/former-faculty',
	     'https://www.bio.iitb.ac.in/people/faculty/','https://www.che.iitb.ac.in/faculty-directory',
	     'https://www.civil.iitb.ac.in/faculty','https://www.me.iitb.ac.in/?q=full-time-faculty',
	     'http://www.esed.iitb.ac.in/faculty-directory','http://www.esed.iitb.ac.in/faculty-directory','https://www.me.iitb.ac.in/?q=honorary-faculty-members',
	     'https://www.phy.iitb.ac.in/en/faculty','https://en.wikipedia.org/wiki/List_of_IIT_Bombay_people',
	     'https://www.iitbbs.ac.in/faculty-members.php',
	     'https://iitpkd.ac.in/faculty-list',
	     'https://iith.ac.in/people/faculty/',
	     'http://www.iitkgp.ac.in/department/AE/faculties'
     	],
    	'query': 'indian engineering faculty names'
    	},

     	
     }

app = Flask(__name__,static_folder='./static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=['GET','POST'])
def index():
	table = None
	table_body = None

	if request.method == 'POST':
		req = request.form
		# print(req)
		req_table = req.to_dict()
		print("==========================================================================================")
		print(req_table)
		print("==========================================================================================")


		if 'dept_name' in req_table:
			session['dept_name'] = req['dept_name']
			# session['dept_name'] = 'All'

			session['research_name'] = ""
			session['web_prev'] = False

		# if 'dept_name' in req_table and 'research_name' in req_table:
		if 'research_name' in req_table:
			# session['dept_name'] = req['dept_name']
			session['dept_name'] = req['research_name']

			deptDict[req['research_name']] = { 
		    	'list':[],
		    	'query': req['research_name']+ ' indian faculty list'
		    }

			session['research_name'] = req['research_name']
			session['web_prev'] = False


		if 'web_prev' in req_table:
			session['web_prev'] = session.get("web_prev") == False


		# dept_name = req['dept_name']
		# research_name = req['research_name']
		
		
		# print(session.get("dept_name"))
		# print(session.get("research_name"))
		table,table_body = DepartmentHardCoded(session.get("dept_name"))
		# table = Department("Aerospace Engineering")
		
		
		# if session.get("research_name")!="":
		# 	filter = []
		# 	for i in table:
		# 		flag = 0
		# 		for j in i:
		# 			if session.get("research_name").lower().replace(" [at] ","@").replace("[at]","@") in j.lower().replace(" [at] ","@").replace("[at]","@"):
		# 				flag = 1
		# 		if flag == 1:
		# 			filter.append(i)
		# 	table = filter

		if 'download-csv' in req_table:
			if(table !=None):
				my_df = pd.DataFrame(table)
				my_df.to_csv('output.csv', index=False, header=False)
				return send_file('output.csv',
                     mimetype='text/csv',
                     attachment_filename='rdp-output.csv',
                     as_attachment=True)


		return render_template("index.html", table = table , len =  len(table) if table else 0 , dept_name=session.get("dept_name"), web_prev = session.get("web_prev"), table_body= table_body )

    # table = iitb_Mech()

	# table = Department("Aerospace Engineering")
	return render_template("index.html" ,len =0)



def getLink(dept_name):
	
	for j in search(deptDict[dept_name]['query'], tld="co.in", num=15, stop=15, pause=2):
	    deptDict[dept_name]['list'].append(j)



def DepartmentHardCoded(dept_name):

	data=[]
	table_body_arr=[]


	getLink(dept_name)
	print(deptDict[dept_name]['list'])
	for link in deptDict[dept_name]['list']:
		
		faculty = requests.get(link, verify=False)
		# faculty = requests.get('https://www.me.iitb.ac.in/?q=full-time-faculty',verify=False)
		facultyContent = faculty.content
		soup_faculty = BeautifulSoup(facultyContent, "html.parser")

		try:

			table_body = soup_faculty.find_all('tbody')
			
			
			for i in table_body:
				table_body_arr.append(i.find_all('tr'))
			# try:
			# print(table_body_arr)

			for i in table_body:
				
				rows = i.find_all('tr')
				for row in rows:
				    cols = row.find_all('td')
				    cols = [ele.text.strip() for ele in cols]
				    data.append([ele for ele in cols if ele])
		except:
			faculty_dic ={}
			for fac in soup_faculty.find_all('div'):
			    if fac not in faculty_dic:
			        faculty_dic[fac] = 1
			    else:
			        faculty_dic[fac] = faculty_dic[fac]+1


			# table_body_arr.append(soup_faculty)
			final = []
			for i,j in faculty_dic.items():
			    if j>1:
			        for k in soup_faculty.find_all('div'):
			            if k == i:
			            	# table_body_arr.append(k)
			            	if k['class'] not in final:
			            		final.append(k['class'])
			for i in final:
			    for j in i:
			        facu = soup_faculty.findAll("div", {"class":j})

			for i in facu:

				if i.text.strip() != "":
					data.append([i.text.strip()])

	return data, table_body_arr
	# except:
	# 	return [], table_body

	# for i in data:
	#     for j in i:
	#         print(j.replace("[at]","@"))
	    # print()



def Department(dept_name):

		url = "https://www.iitb.ac.in/en/education/academic-divisions"

		r = requests.get(url, verify=False)
		htmlContent = r.content
		soup = BeautifulSoup(htmlContent, "html.parser")
		

		for list in soup.findAll('a'):
		    if list.text.strip() == dept_name:
		        
		        d = str(list.get('href'))
		        # print(d)
		        dept = requests.get(d,verify=False)
		        deptContent = dept.content
		        soup_dept = BeautifulSoup(deptContent,"html.parser")

		for list in soup_dept.findAll('a'):
		    if list.text.strip() == "Faculty":
		        f = list.get('href')
		        # print(f)
		        try:
		            faculty = requests.get(f,verify=False)
		        except:
		            faculty = requests.get(d+f, verify=False)
		        # faculty = requests.get('https://www.me.iitb.ac.in/?q=full-time-faculty',verify=False)
		        facultyContent = faculty.content
		        soup_faculty = BeautifulSoup(facultyContent, "html.parser")


		table_body = soup_faculty.find('tbody')
		# print(table_body)
		try:
			data=[]
			rows = table_body.find_all('tr')
			for row in rows:
			    cols = row.find_all('td')
			    cols = [ele.text.strip() for ele in cols]
			    data.append([ele for ele in cols if ele])

			return data, table_body
		except:
			return [], table_body

	# for i in data:
	#     for j in i:
	#         print(j.replace("[at]","@"))
	    # print()



def iitb_Mech():
	# url = "https://www.cse.iitb.ac.in/people/faculty.php"
	# url = "https://www.me.iitb.ac.in/?q=full-time-faculty"
	# url = "https://www.aero.iitb.ac.in/home/people/faculty"
	# url= "https://ar.iitr.ac.in/departments/AR/pages/People+Faculty_List.html"
	url = "http://www.ae.iitm.ac.in/files/faculty.html"
	result = requests.get(url).text
	doc = BeautifulSoup(result, "html.parser")


	table = doc.find_all("table")


	tableBody = doc.tbody
	# trs = tableBody.contents

	# faculty_data = []

	# for tr in trs:
	# 	try:
	# 		name,image,phone_no,email,research = tr.find_all("td")
	# 		# print(tr.find_all("td"))
	# 		faculty_data.append({
	# 			"name": name.a.string,
	# 			"link": "https://www.me.iitb.ac.in"+name.a["href"],
	# 			"image": image.p.a.img["src"],
	# 			"phone_no": phone_no.string.strip(),
	# 			"email": email.h4.string,
	# 			"research": research.p.string.split(","),
	# 			})
	# 		# print(name.a.string,image.p.a.img["src"],phone_no.string.strip(),email.h4.string,research.p.string.split(","))
	# 	except:
	# 		pass

	# print(table[0])
	return table



if __name__ == "__main__":
	app.run(debug=True,port="5000")

