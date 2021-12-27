import requests, sys, webbrowser, bs4

req = requests.get("https://www.google.com/search?q=iit+faculty+names&oq=iit+faculty+names&aqs=chrome.0.69i59.109j0j1&sourceid=chrome&ie=UTF-8")

req.raise_for_status()

soup = bs4.BeautifulSoup(req.text,"html.parser")




linkElement = soup.find_all("div",class_="yuRUbf")
# linkToOpen = min(5,len(linkElement))

# print("==================")
print(soup)


# for i in range(0,10):
# 	# webbrowser.open('https://google.com'+linkElement[i].get('href'))
# 	print(linkElement[i].get('href'))




