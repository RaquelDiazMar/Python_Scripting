import requests

#Reading a specific webpage

def readUrlContent():
    url= "https://www.google.com"
    content = requests.get(url)
    print(content.text)
    
readUrlContent()

##############################################

#Reading any webpage

def readAnyUrlContent(url):
    content = requests.get(url)
    print(content.text)

readAnyUrlContent("https://www.google.com")

