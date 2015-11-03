import urllib.request
from bs4 import BeautifulSoup
import json

from users import Users
from users import Repos

def readUsers(URL):

	req = urllib.request.Request(URL)
	with urllib.request.urlopen(req) as response:
	   the_page = response.read()

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


for i,j in Users.items():
	print (j.userName)

