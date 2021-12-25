import requests
from bs4 import BeautifulSoup
import re
url = ["https://www.google.com/search?q=iit+faculties"]

#path:  home page --> Academics --> Department --> People --> faculty

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")

faculty_link = []

for link in soup.find_all('a'):
    if re.findall('faculty',str(link.get('href'))):
        faculty_link.append(link.get("href"))

for academics in faculty_link:
    # print(academics+"\n\n")
    a = requests.get(url+academics)
    a_content = a.content
    soup_academics =  BeautifulSoup(a_content, "html.parser")
    for i in soup_academics.findAll('a'):
        if re.findall('Academic',str(i.get('href'))):
            print(i.get('href'))
