class Users(dict):
	def __init__(self,lastid):
		self.lastid = lastid


class Repos(dict):
	def __init__(self,userName):
		self.userName = userName
		self.getRepos(userName)


	def getRepos(self,userName):
		repoURL = 'https://api.github.com/users/' + userName+'/repos'


		print(repoURL)