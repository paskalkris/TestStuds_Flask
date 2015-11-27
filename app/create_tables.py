from .groups.models import Group
from .students.models import Stud
from .init_db import database

def create_tables():
    database.db.connect()
    database.db.create_tables([Group, Stud])
    database.db.create_foreign_key(Group, Group.starosta)