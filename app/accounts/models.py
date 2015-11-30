from peewee import Model, CharField, DateTimeField
from app.init_db import database


class User(database.Model):
    username = CharField(verbose_name="Пользователь", unique=True)
    password = CharField(verbose_name="Пароль")
    join_date = DateTimeField()

    class Meta:
        order_by = ('username',)

    def __str__(self):
        return self.username
