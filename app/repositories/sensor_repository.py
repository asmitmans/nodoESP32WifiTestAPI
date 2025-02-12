from sqlalchemy.exc import OperationalError
from app import db
from app.models.sensor_data import SensorData
import logging

logger = logging.getLogger(__name__)

def save_sensor_data(sensor_data):
    try:
        db.session.add(sensor_data)
        db.session.commit()
    except OperationalError:
        logger.error("Error de conexión con la base de datos. PostgreSQL podría estar apagado.")
        raise Exception("No se pudo conectar a la base de datos.")
    except Exception as e:
        logger.error(f"Error interno en la base de datos: {e}")
        raise Exception("Error al procesar la solicitud en la base de datos.")

def get_all_sensor_data():
    try:
        return SensorData.query.all()
    except Exception as e:
        logger.error(f"Error al obtener datos: {e}")
        return []
