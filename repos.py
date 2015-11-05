import json
from bs4 import BeautifulSoup

from AuthoRequest import AuthoRequest


class Repos(dict):
    pass


class repo(object):
    def __init__(self, repoName):
        self.repoName = repoName
        self.repoJson = 'empty'

    def setRepoJson(self, repoJson):
        self.repoJson = repoJson
        self.language = str(repoJson['language'])
