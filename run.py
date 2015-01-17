import os
from server import app

def runserver():
	heroku = int(os.environ.get('HEROKU', 0))
	if (heroku != 0):
		print "Running on Heroku"
		app.run(host='0.0.0.0')
	else:
		print "Running locally"
		port = int(os.environ.get('PORT', 5000))
		app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    runserver()