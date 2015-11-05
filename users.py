from bs4 import BeautifulSoup
import json

from repos import Repos, repo
from AuthoRequest import AuthoRequest


class Users(dict):
    def __init__(self, lastid):
        self.lastid = lastid


class user(object):
    def __init__(self, userName):
        self.userName = userName
        self.userJson = self.getUserJson(userName)
        self.parseJson()
        self.createRepos()

    def getUserJson(self, userName):
        userURL = 'https://api.github.com/users/' + userName
        the_page = AuthoRequest(userURL)
        soup = BeautifulSoup(the_page, "html5lib")
        reposJson = json.loads(soup.get_text())
        return(reposJson)

    def parseJson(self):
        self.name = self.userJson['name']
        self.public_repos = self.userJson['public_repos']
        self.hireable = self.userJson['hireable']

    def createRepos(self):
        self.Repos = Repos()
        userURL = 'https://api.github.com/users/' + self.userName + '/repos'
        the_page = AuthoRequest(userURL)
        soup = BeautifulSoup(the_page, "html5lib")
        reposJson = json.loads(soup.get_text())
        for i in reposJson:
            repoName = i["name"]
            self.Repos[repoName] = repo(repoName)
            self.Repos[repoName].setRepoJson(i)
