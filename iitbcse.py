from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template, request, redirect
from requests.packages.urllib3.exceptions import InsecureRequestWarning

app = Flask(__name__,static_folder='./static')

@app.route("/", methods=['GET','POST'])
def index():
	table = None
	if request.method == 'POST':
		req = request.form
		dept_name = req['dept_name']
		print(dept_name)
		table = Department(dept_name)
		# table = Department("Aerospace Engineering")


		return render_template("index.html", table = table , len= len(table))

    # table = iitb_Mech()

	# table = Department("Aerospace Engineering")
	return render_template("index.html")




def Department(dept_name):

	try:
		url = "https://www.iitb.ac.in/en/education/academic-divisions"

		r = requests.get(url, verify=False)
		htmlContent = r.content
		soup = BeautifulSoup(htmlContent, "html.parser")
		

		for list in soup.findAll('a'):
		    if list.text.strip() == dept_name:
		        
		        d = str(list.get('href'))
		        print(d)
		        dept = requests.get(d,verify=False)
		        deptContent = dept.content
		        soup_dept = BeautifulSoup(deptContent,"html.parser")

		for list in soup_dept.findAll('a'):
		    if list.text.strip() == "Faculty":
		        f = list.get('href')
		        print(f)
		        try:
		            faculty = requests.get(f,verify=False)
		        except:
		            faculty = requests.get(d+f, verify=False)
		        facultyContent = faculty.content
		        soup_faculty = BeautifulSoup(facultyContent, "html.parser")

		table_body = soup_faculty.find('tbody')
		data=[]
		rows = table_body.find_all('tr')
		for row in rows:
		    cols = row.find_all('td')
		    cols = [ele.text.strip() for ele in cols]
		    data.append([ele for ele in cols if ele])

		return data	
	except:
		return "Data not found"

	# for i in data:
	#     for j in i:
	#         print(j.replace("[at]","@"))
	    # print()


def iitb_Mech():
	# url = "https://www.cse.iitb.ac.in/people/faculty.php"
	# url = "https://www.me.iitb.ac.in/?q=full-time-faculty"
	# url = "https://www.aero.iitb.ac.in/home/people/faculty"
	# url= "https://ar.iitr.ac.in/departments/AR/pages/People+Faculty_List.html"
	url = "http://www.ae.iitm.ac.in/files/faculty.htm"
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
    app.run(host='127.0.0.1',port=4455,debug=True)

