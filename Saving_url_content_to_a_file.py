import requests
import urllib.request

def saveUrlContent():
    url = "https://www.google.com"
    content = urllib.request.urlopen(url)
    data = content.read()
    with open('urlData.html', 'wb') as file: 
    #if websiteData.html does not exist yet, it will be created, otherwise, it will be overwritten
        file.write(data)
                
saveUrlContent()

#####################################################

def saveAnyUrlContent(url):
    content = urllib.request.urlopen(url)
    data = content.read()
    with open('urlData.html', 'wb') as file: #if websiteData.html does not exist yet, it will be created, otherwise, it will overwrite it
        file.write(data)

saveAnyUrlContent("https://www.google.com")
