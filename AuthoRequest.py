from getUnamePassAuth import unamePass
from urllib.request import build_opener, HTTPSHandler, HTTPError, Request
import base64
def AuthoRequest(url):
	username,password = unamePass()
	userandpass = base64.b64encode(bytes('%s:%s' % (username, password), 'utf-8'))
	userandpass = userandpass.decode('ascii')
	authorization = 'Basic %s' % userandpass
	opener = build_opener(HTTPSHandler)
	request = Request(url)
	request.add_header('Authorization', authorization)
	response = opener.open(request)
	return response.read()