import urllib.request
from bs4 import BeautifulSoup
import json

from AuthoRequest import AuthoRequest

class Users(dict):
	def __init__(self,lastid):
		self.lastid = lastid


class user(object):
	def __init__(self,userName):
		self.userName = userName
		self.userJson = self.getUserJson(userName)
		self.parseJson()


	def getUserJson(self,userName):
		repoURL = 'https://api.github.com/users/' + userName
		the_page = AuthoRequest(repoURL)
		soup = BeautifulSoup(the_page, "html5lib")
		reposJson = json.loads(soup.get_text())
		return(reposJson)

	def parseJson(self):
		self.name = self.userJson['name']
		self.public_repos = self.userJson['public_repos']
		self.hireable = self.userJson['hireable']
