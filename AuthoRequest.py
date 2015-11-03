try:

	from getUnamePassAuth import unamePass 
	#if this file with username and password exists
	# authenticate otherwise dont.
	print('Authenticating . . .')
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

except ImportError:
	from urllib.request import Request, urlopen
	print('Not Authenticating . . .')
	def AuthoRequest(url):
		req = Request(url)
		with urlopen(req) as response:
		   the_page = response.read()

		return the_page


