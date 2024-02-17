from bottle import route, run, template 

#get route for home page, should be a page to login with spotify account
@route('/', method='GET') 
def login(): 
	#should be a form here / button to just login
	return template('View/index.tpl') 

#post route for when login happens, redirect to select playlist page
@route('/', method='POST') 
def doLogin(): 
	#handle spotify login logic, redirect to get method on fail, redirect to playlist select on succeed
	return template('View/index.tpl') 

#
@route('/select', method='GET')
def select():

	return template('View/select.tpl')

run(host='localhost', port=8080,debug=True)
