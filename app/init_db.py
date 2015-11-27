from peewee import SqliteDatabase, Model
from flask import current_app as app


class DataBase():
    def __init__ (self):
        self.db = None
        self.model = None

    def init_db(self, app):
        self.db = SqliteDatabase(app.config['DATABASE'])
        self.Model = self.get_model_class()

        @app.before_request
        def before_request():
            self.db.connect()

        @app.after_request
        def after_request(response):
            self.db.close()
            return response

    def get_model_class(self):
        class BaseModel(Model):
            class Meta:
                database = self.db

        return BaseModel


database = DataBase()

