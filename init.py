from src.app import app
from src.db.db import db

from src.db.models import post , subscribsion , code

with app.app_context():
    db.create_all()