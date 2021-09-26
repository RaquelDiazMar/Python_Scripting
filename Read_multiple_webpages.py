import requests
import urllib.request

def crawlPage():
    for i in range(1451720, 1451730):
        url = "https://www.mmo-champion.com/members/" + str(i)
        f = requests.get(url)
        print(f.text)

crawlPage()

######################################################################

def crawlAnyPage(url, start, stop):
    for i in range(start, stop):
        url = url + str(i)
        f = requests.get(url)
        print(f.text)

crawlAnyPage("https://www.mmo-champion.com/members/", 1451720, 1451730)
