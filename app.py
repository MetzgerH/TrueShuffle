from bottle import route, run, template 


@route('/') 
def index(): 
	return template('View/index.tpl') 


run(host='localhost', port=8080,debug=True)
