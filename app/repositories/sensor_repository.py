from app import db
from app.models.sensor_data import SensorData
from sqlalchemy.exc import SQLAlchemyError


def save_sensor_data(sensor_data):
    try:
        db.session.add(sensor_data)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()  
        print(f"Error al guardar en DB: {str(e)}")

def get_all_sensor_data():
    try:
        return SensorData.query.all()
    except SQLAlchemyError as e:
        print(f"Error al recuperar datos de DB: {str(e)}")
        return []
