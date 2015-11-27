from peewee import Model, CharField, ForeignKeyField
from app.init_db import database
#from app.students.models import Stud

from .proxy import StudProxy


class Group(database.Model):
    name = CharField(verbose_name="Наименование", max_length=16, unique=True)
    starosta = ForeignKeyField(StudProxy, null=True, verbose_name="Староста")

    def __str__(self):
        return self.name
