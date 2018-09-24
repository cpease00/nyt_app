from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash
# initialized new flask app
server = Flask(__name__)
# added configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# connected flask_sqlalchemy to the configured flask app
db = SQLAlchemy(server)
from package.model import *

app=dash.Dash(__name__, server=server, url_base_pathname = '/')
#to run html templates:
#from package import dashlayout
from package.dashview import app
