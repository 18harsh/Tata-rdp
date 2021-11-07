import requests
from bs4 import BeautifulSoup
from requests.api import request
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://iitr.ac.in/Main/pages/_en_Departments__en_.html"

r = requests.get(url, verify=False)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")

dept_name = 'Mathematics'
print("\n")
# for dept_name in departments:
print(dept_name)
for list in soup.findAll('a'):
    if list.text.strip() == dept_name:
        try:
            d = "https:" + str(list.get('href'))
            print(d)
            dept = requests.get(d,verify=False)
        except:
            d = url+ str(list.get('href'))
            print(d)
            dept = requests.get(url+d,verify=False)
        deptContent = dept.content
        soup_dept = BeautifulSoup(deptContent,"html.parser")

print(soup_dept)