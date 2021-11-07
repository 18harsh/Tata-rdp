import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re 

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://www.iitb.ac.in/en/education/academic-divisions"

r = requests.get(url, verify=False)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")
# ['Aerospace Engineering',
# 'Biosciences and Bioengineering',
# 'Chemical Engineering'
# 'Chemistry',
# 'Civil Engineering',
# 'Computer Science & Engineering',
# 'Earth Sciences',
# 'Electrical Engineering',
# 'Energy Science and Engineering',
# 'Environmental Science and Engineering (ESED)',
# 'Humanities & Social Sciences',
# 'Mathematics',
# 'Mechanical Engineering',
# 'Metallurgical Engineering & Materials Science',
# 'Physics']

departments = ['Chemical Engineering']

# dept_name = input()
print("\n")
for dept_name in departments:
    print(dept_name+"-------------------------------+=+++++++++++++")
    try:
        for list in soup.findAll('a'):
            if list.text.strip() == dept_name:
                d = str(list.get('href'))
                dept = requests.get(d,verify=False)
                deptContent = dept.content
                soup_dept = BeautifulSoup(deptContent,"html.parser")

        for list in soup_dept.findAll('a'):
            if list.text.strip() == "Faculty":
                f = list.get('href')
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
                print(j) 
            print("====================================================")
    except:
        for list in soup.findAll('a'):
            if list.text.strip() == dept_name:
                d = str(list.get('href'))
                dept = requests.get(d,verify=False)
                deptContent = dept.content
                soup_dept = BeautifulSoup(deptContent,"html.parser")

        for list in soup_dept.findAll('a'):
            if list.text.strip() == "Faculty":
                f = list.get('href')
                try:
                    faculty = requests.get(f,verify=False)
                except:
                    faculty = requests.get(d+f, verify=False)
                facultyContent = faculty.content
                soup_faculty = BeautifulSoup(facultyContent, "html.parser")
        faculty_dic = {}
        divs = soup_faculty.find_all(['p','h2'])
        for fac in divs:
            print(fac.text.strip())
        #     if fac not in faculty_dic:
        #         faculty_dic[fac] = 1
        #     else:
        #         faculty_dic[fac] = faculty_dic[fac]+1

        # # final = []

        # for i,j in faculty_dic.items():
        #     if j>1:
        #         soup_faculty.find_all('div')
        
        # print(final)




# for list in soup.findAll('a'):
#     if list.text.strip() == dept_name:
        
#         d = str(list.get('href'))
#         print(d)
#         dept = requests.get(d,verify=False)
#         deptContent = dept.content
#         soup_dept = BeautifulSoup(deptContent,"html.parser")

# for list in soup_dept.findAll('a'):
#     if list.text.strip() == "Faculty":
#         f = list.get('href')
#         print(f)
#         try:
#             faculty = requests.get(f,verify=False)
#         except:
#             faculty = requests.get(d+f, verify=False)
#         facultyContent = faculty.content
#         soup_faculty = BeautifulSoup(facultyContent, "html.parser")

# table_body = soup_faculty.find('tbody')
# data=[]
# rows = table_body.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append([ele for ele in cols if ele])

# for i in data:
#     for j in i:
#         print(j.replace("[at]","@"))
#     print()
