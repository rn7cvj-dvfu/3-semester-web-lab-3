import os
from dotenv import load_dotenv

load_dotenv()

POSTS_ON_PAGE = 20

BOT_TOKEN = os.getenv("BOT_TOKEN") 
SECRET_KEY = os.getenv("SECRET_KEY") 
DATABASE_URL = "sqlite:///wall.db"
SESSION_TYPE = "filesystem"


BASE_URL = os.getenv("BASE_URL")

CODE_LENGTH = 6
CODE_ADDED_NUMBERS = 2

CODE_LIFE_TIME = 120 # in seconds