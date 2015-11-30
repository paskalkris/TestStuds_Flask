from flask import Flask, g
from peewee import SqliteDatabase, SQLITE_DATETIME_FORMATS
from .init_db import database


app = Flask(__name__)
app.config.from_object('config')

database.init_db(app)

from .groups.views import bp as bp_group
from .students.views import bp as bp_stud
from .accounts.views import bp as bp_acc
app.register_blueprint(bp_group, url_prefix='/groups')
app.register_blueprint(bp_stud, url_prefix='/students')
app.register_blueprint(bp_acc, url_prefix='/acc')

#db = SqliteDatabase(app.config['DATABASE'])

#from groups import views
#from .groups import models

#def create_tables():
#    db.connect()
#    db.create_table(models.Group)


