import os
from server import app
from server.db import db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from server.models import *

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand) # sets 'db' as symbol for command-line invocation of migrations

if __name__ == '__main__':
    manager.run()