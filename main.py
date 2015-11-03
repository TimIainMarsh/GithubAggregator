
from urllib.request import build_opener, HTTPSHandler, HTTPError, Request
from urllib.parse import quote as urlquote

import base64

from bs4 import BeautifulSoup
import json

from users import Users
from users import user
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
# while Users.lastid <= 45:
# 	startURL = 'https://api.github.com/users?since=' + str(Users.lastid)
# 	UsersList,lastid = readUsers(startURL)
# 	Users.lastid = lastid
# 	for item in UsersList:
# 		Users[item] = user(item)
		

Users['TimIainMarsh'] = user('TimIainMarsh')
Users['jasrusable'] = user('jasrusable')
Users['CraigNielsen'] = user('CraigNielsen')
Users['avoid3d'] = user('avoid3d')

for i,j in Users.items():
	print ( str(j.name) + "  " + str(j.public_repos) )

