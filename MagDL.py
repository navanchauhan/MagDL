from bs4 import BeautifulSoup
import re
import requests


#userInput = "Computer Active"
userInput = input("Enter your Input: \n")

searchTerm = userInput.replace(" ", "+")
firstWord = userInput.split(' ', 1)[0].lower() 

url = "https://magazinelib.com/?s=" + searchTerm


response = requests.get(url)
page = str(BeautifulSoup(response.content, "lxml"))

allLinks = []
links = []

def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        allLinks.append(url)
    else:
        break


for a in allLinks:
    x = re.search("all/" + firstWord, a)
    if(x != None):
        links.append(a)

def printLinks(n):
    i = 0
    while (i<n) :
        print("[", i, "]", (links[i].replace("https://magazinelib.com/all/","")).replace("/","").replace("-"," "))
        i +=1

printLinks(10)

choice = eval(input("Enter the index number: \n"))

dl = []

url = links[choice]
print(links[choice])
response = requests.get(url)
page = str(BeautifulSoup(response.content, "lxml"))

while True:
    url, n = getURL(page)
    page = page[n:]
    if url:
        dl.append(url)
    else:
        break

for a in dl:
    x = re.search("vk.com", a)
    if(x != None):
        print(a)



