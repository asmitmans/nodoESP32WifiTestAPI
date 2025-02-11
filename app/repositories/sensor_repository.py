from app import db
from app.models.sensor_data import SensorData
import logging

logger = logging.getLogger(__name__)

def save_sensor_data(sensor_data):
    try:
        db.session.add(sensor_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error al guardar en BD: {e}")
        raise Exception("Error interno al guardar en la base de datos.")

def get_all_sensor_data():
    try:
        return SensorData.query.all()
    except Exception as e:
        logger.error(f"Error al obtener datos: {e}")
        return []
