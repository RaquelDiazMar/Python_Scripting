import requests
import urllib.request

def saveUrlContent():
    url = "https://www.google.com"
    content = urllib.request.urlopen(url)
    data = content.read()
    with open('urlData.html', 'wb') as file: 
    #Note1: if websiteData.html does not exist yet, it will be created, otherwise, it will be overwritten
    #Note2: the open() function opens a file in text format by default. To open a file in binary format, add 'b' 
    #to the mode parameter. Hence the "wb" mode opens the file in binary format for writing.  
        file.write(data)
                
saveUrlContent()

#####################################################

def saveAnyUrlContent(url):
    content = urllib.request.urlopen(url)
    data = content.read()
    with open('urlData.html', 'wb') as file:
        file.write(data)

saveAnyUrlContent("https://www.google.com")
