import urllib.request
from bs4 import BeautifulSoup
import json

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

		req = urllib.request.Request(repoURL)
		with urllib.request.urlopen(req) as response:
			the_page = response.read()

		soup = BeautifulSoup(the_page, "html5lib")
		reposJson = json.loads(soup.get_text())

		return(len(reposJson))
		# print(reposJson[1]['name'])

