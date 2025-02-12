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
        logger.error("Error de conexión con la base de datos. Verifica si PostgreSQL está en ejecución.")
        raise Exception("No se pudo conectar a la base de datos.")  # Lanzar excepción controlada
    except Exception as e:
        logger.error(f"Error interno al guardar en la base de datos: {str(e)}")
        raise Exception("Error interno al guardar en la base de datos.")  # Lanzar excepción controlada

def get_all_sensor_data():
    try:
        return SensorData.query.all()
    except Exception as e:
        logger.error(f"Error al obtener datos: {e}")
        return []
