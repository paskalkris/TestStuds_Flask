#!flask/bin/python
from app import app
from app.create_tables import create_tables

#create_tables()
app.debug = True
app.run(host = '0.0.0.0', port=8000)