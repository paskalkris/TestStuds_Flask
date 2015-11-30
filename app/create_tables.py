from .groups.models import Group
from .students.models import Stud
from .accounts.models import User
from .init_db import database

def create_tables():
    database.db.connect()
    database.db.create_table(User)
    #database.db.create_tables([Group, Stud, User])
    #database.db.create_foreign_key(Group, Group.starosta)