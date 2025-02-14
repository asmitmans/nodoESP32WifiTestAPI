from app import create_app
from app.config import Config

app = create_app()

if __name__ == '__main__':
    app.run(host=Config.FLASK_RUN_HOST, port=Config.FLASK_RUN_PORT)
