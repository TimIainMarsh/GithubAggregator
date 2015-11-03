
from urllib.request import build_opener, HTTPSHandler, HTTPError, Request
from urllib.parse import quote as urlquote

import base64

from bs4 import BeautifulSoup
import json

from users import Users
from users import Repos
from AuthoRequest import AuthoRequest

def readUsers(URL):

	the_page = AuthoRequest(URL)

	soup = BeautifulSoup(the_page, "html5lib")
	usersJson = json.loads(soup.get_text())
	USERS = []
	for i in usersJson:
		USERS.append(i['login'])
	lastid = usersJson[len(usersJson)-1]['id']
	return USERS, lastid



Users = Users(0)
while Users.lastid <= 45:
	startURL = 'https://api.github.com/users?since=' + str(Users.lastid)
	UsersList,lastid = readUsers(startURL)
	Users.lastid = lastid
	for user in UsersList:
		Users[user] = Repos(user)
		

Users['TimIainMarsh'] = Repos('TimIainMarsh')
for i,j in Users.items():
	print (i+ ' ' +str(j.numberOfrepos))

