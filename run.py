import os
from server import app

def runserver():
	heroku = int(os.environ.get('HEROKU', 0))
	print heroku
	if (heroku != 0):
		print "On Heroku"
		app.run(host='0.0.0.0')
	else:
		print "NOT on Heroku"
		port = int(os.environ.get('PORT', 5000))
		app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    runserver()