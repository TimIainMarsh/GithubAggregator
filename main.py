class Users(dict):
	def __init__(self,lastid):
		self.lastid = lastid


import urllib2
from bs4 import BeautifulSoup
import json

def readUsers(URL):
	page = urllib2.urlopen(URL).read()
	soup = BeautifulSoup(page, "lxml")
	usersJson = json.loads(soup.get_text())
	USERS = []
	for i in usersJson:
		# print i
		USERS.append(i['login'])
	lastid = usersJson[len(usersJson)-1]['id']
	print(lastid)
	return USERS, lastid

Users = Users(0)

while Users.lastid <= 100:
	startURL = 'https://api.github.com/users?since=' + str(Users.lastid)
	print startURL
	USERS,lastid = readUsers(startURL)
	Users.lastid = lastid

print(Users)
# print USERS
# for i in USERS:


# for i in USERS:
# 	print (i)
# 	print("-----------------------------------------------------------------------------")


# print (API)

# users = User(API[0][u'login'], API[0][u'name'], API)



# print(API[u'login'])
# print(API[u'public_repos'])

