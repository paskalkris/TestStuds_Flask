'''from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)
app.config.from_object('config')
db = SqliteDatabase(app.config['DATABASE'])
from groups import views
from groups import models

def create_tables():
    db.connect()
    db.create_table(models.Group)

'''