from peewee import Model, CharField, DateField, ForeignKeyField
from app.init_db import database

from app.groups.models import Group
from app.groups.proxy import StudProxy


class Stud(database.Model):
    name = CharField(verbose_name="ФИО", max_length=128)
    dbirthday = DateField(verbose_name="Дата рождения")
    nstud = CharField(verbose_name="Студенческий билет", max_length=15, unique=True)
    cgroup = ForeignKeyField(Group, verbose_name="Группа")

    def __str__(self):
        return self.name

StudProxy.initialize(Stud)
