import os
import json
from flask import Flask, request, Response

app = Flask(__name__, static_folder='../client/static', template_folder='../client/views')

os.environ['APP_SETTINGS'] = 'server.config.DevelopmentConfig' # needs to be dynamic
app.config.from_object(os.environ['APP_SETTINGS'])

import server.api
import server.controllers
from server.db import db