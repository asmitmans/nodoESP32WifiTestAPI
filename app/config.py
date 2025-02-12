from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
