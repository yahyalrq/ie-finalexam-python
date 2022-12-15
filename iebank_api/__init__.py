from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
load_dotenv()



db = SQLAlchemy(app)

from iebank_api.models import Account
db.create_all()
CORS(app)

from iebank_api import routes