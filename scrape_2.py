import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://www.iitb.ac.in/en/education/academic-divisions"

r = requests.get(url, verify=False)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")


# dept_name = input()
dept_name = "Aerospace Engineering"
print("\n")

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

for i in data:
    for j in i:
        print(j.replace("[at]","@"))
    print()