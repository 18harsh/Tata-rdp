from bs4 import BeautifulSoup
import requests
from flask import Flask,render_template, request, redirect


app = Flask(__name__,static_folder='./static')

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return render_template("index.html")

    table = iitb_Mech()

    return render_template("index.html", table = table)


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

