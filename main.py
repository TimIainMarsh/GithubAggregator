
from urllib.request import build_opener, HTTPSHandler, HTTPError, Request
from urllib.parse import quote as urlquote
import base64, json
from bs4 import BeautifulSoup

from users import Users, user
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
#   startURL = 'https://api.github.com/users?since=' + str(Users.lastid)
#   UsersList,lastid = readUsers(startURL)
#   Users.lastid = lastid
#   for item in UsersList:
#       Users[item] = user(item)

Users['TimIainMarsh'] = user('TimIainMarsh')
Users['jasrusable'] = user('jasrusable')
Users['CraigNielsen'] = user('CraigNielsen')
Users['avoid3d'] = user('avoid3d')

for uname, user_thing in Users.items():
    print(str(user_thing.name) + "  " + str(user_thing.public_repos))
    for repoN, repo in user_thing.Repos.items():
        print('--'+str(repo.repoName)+' '+repo.language)
