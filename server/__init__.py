import os
import json
from flask import Flask, request, Response

print "In __init__"

app = Flask(__name__, static_folder='../client/static', template_folder='../client/views')

on_heroku = int(os.environ.get('HEROKU', 0)) != 0

if on_heroku:
	print "On Heroku"
	os.environ['APP_SETTINGS'] = 'server.config.ProductionConfig'
else:
	os.environ['APP_SETTINGS'] = 'server.config.DevelopmentConfig'

app.config.from_object(os.environ['APP_SETTINGS'])

import server.api
import server.controllers
from server.db import db