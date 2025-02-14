from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Inicializar extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos y migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints con prefijo '/api'
    from app.controllers.sensor_controller import sensor_bp
    app.register_blueprint(sensor_bp, url_prefix='/api')

    return app
