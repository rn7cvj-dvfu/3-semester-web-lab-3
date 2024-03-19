from flask import Flask 
from flask_header_session import Session

from src.config import SECRET_KEY , DATABASE_URL , SESSION_TYPE



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SESSION_TYPE'] = SESSION_TYPE
