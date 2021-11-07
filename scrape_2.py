import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.corpus import stopwords

stop = stopwords.words('english')

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




# def extract_phone_numbers(string):
#     r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
#     phone_numbers = r.findall(string)
#     return phone_numbers

# def extract_email_addresses(string):
#     r = re.compile(r'[\w\.-]+@[\w\.-]+')
#     return r.findall(string)

# def ie_preprocess(document):
#     document = ' '.join([i for i in document.split() if i not in stop])
#     sentences = nltk.sent_tokenize(document)
#     sentences = [nltk.word_tokenize(sent) for sent in sentences]
#     sentences = [nltk.pos_tag(sent) for sent in sentences]
#     return sentences

# def extract_names(document):
#     names = []
#     sentences = ie_preprocess(document)
#     for tagged_sentence in sentences:
#         for chunk in nltk.ne_chunk(tagged_sentence):
#             if type(chunk) == nltk.tree.Tree:
#                 if chunk.label() == 'PERSON':
#                     names.append(' '.join([c[0] for c in chunk]))
#     return names



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

<<<<<<< HEAD
departments = ['Civil Engineering']
=======
departments = ['Chemical Engineering']

# dept_name = input()
>>>>>>> 127f617170a429245883a3758c2f0ced48885134
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
                f = list.get('href').replace(".php","")
                try:
                    faculty = requests.get(f,verify=False)
                except:
                    print(d+f)
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
        # faculty_dic = {}
        # for fac in soup_faculty.contents:
        #     s = str(fac.text.strip())
        #     print("---------------")
        #     print(s)
        #     print("===============")
        #     if (extract_names(s), extract_phone_numbers(s),extract_email_addresses(s)) not in faculty_dic:
        #         faculty_dic.append([extract_names(s), extract_phone_numbers(s),extract_email_addresses(s)])

        # for i in faculty_dic:
        #     print(i)

            # numbers = extract_phone_numbers(s)
            # emails = extract_email_addresses(s)
            # names = extract_names(s)
            # print(names, emails, numbers)
        data = []
        faculty_dic ={}
        for fac in soup_faculty.find_all('div'):
            if fac not in faculty_dic:
                faculty_dic[fac] = 1
            else:
                faculty_dic[fac] = faculty_dic[fac]+1

        
        final = []
        for i,j in faculty_dic.items():
            if j>1:
                for k in soup_faculty.find_all('div'):
                    if k == i:
                        if k['class'] not in final:
                            final.append(k['class'])
        for i in final:
            for j in i:
                facu = soup_faculty.findAll("div", {"class":j})

        for i in facu:
            if i.text.strip()!=' ':
                data.append([i.text.strip()])
        print(data)   
        

        
                        
        #deptDict = {
# 	'Aerospace Engineering': ['https://www.aero.iitb.ac.in/home/people/faculty'],
#     'Biosciences and Bioengineering':['https://www.bio.iitb.ac.in/people/faculty/'],
#     'Chemical Engineering':['https://www.che.iitb.ac.in/faculty-directory'],
#     'Chemistry':[],
#     'Civil Engineering':['https://www.civil.iitb.ac.in/faculty'],
#     'Computer Science & Engineering':[],
#     'Earth Sciences':[],
#     'Electrical Engineering':[],
#     'Energy Science and Engineering':['https://www.me.iitb.ac.in/?q=full-time-faculty'],
#     'Environmental Science and Engineering (ESED)':['http://www.esed.iitb.ac.in/faculty-directory'],
#     'Humanities & Social Sciences':[],
#     'Mathematics':[],
#     'Mechanical Engineering':['http://www.esed.iitb.ac.in/faculty-directory','https://www.me.iitb.ac.in/?q=honorary-faculty-members'],
#     'Metallurgical Engineering & Materials Science':[],
#     'Physics':['https://www.phy.iitb.ac.in/en/faculty'],
    
# }




<<<<<<< HEAD
=======
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
>>>>>>> 127f617170a429245883a3758c2f0ced48885134
