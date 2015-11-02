import urllib2
from bs4 import BeautifulSoup
import json

page = urllib2.urlopen('https://api.github.com/users/TimIainMarsh').read()

soup = BeautifulSoup(page, "lxml")

API = json.loads(soup.get_text())

# print (API)

print(API[u'login'])
print(API[u'public_repos'])