from flask_sqlalchemy import SQLAlchemy
from src.app import app


db = SQLAlchemy()
db.init_app(app)