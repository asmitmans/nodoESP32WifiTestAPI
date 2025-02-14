from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '127.0.0.1')   # Valor por defecto: localhost
    FLASK_RUN_PORT = int(os.getenv('FLASK_RUN_PORT', 5000))     # Valor por defecto: 5000
