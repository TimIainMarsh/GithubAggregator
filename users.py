import urllib.request
from bs4 import BeautifulSoup
import json

from AuthoRequest import AuthoRequest

class Users(dict):
	def __init__(self,lastid):
		self.lastid = lastid


class Repos(dict):
	def __init__(self,userName):
		self.userName = userName
		# self.getRepos(userName)
		self.numberOfrepos = self.getRepos(userName)

	def getRepos(self,userName):
		repoURL = 'https://api.github.com/users/' + userName+'/repos'
		
		the_page = AuthoRequest(repoURL)

		soup = BeautifulSoup(the_page, "html5lib")
		reposJson = json.loads(soup.get_text())

		return(len(reposJson))
		# print(reposJson[1]['name'])

