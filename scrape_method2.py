import requests
from bs4 import BeautifulSoup
import webbrowser
from googlesearch import search
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



dept = input("Enter Department")
university = input("Enter University")
query = dept + " " + university + " research faculty in India"

url_list = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    url_list.append(j)

print(url_list)

