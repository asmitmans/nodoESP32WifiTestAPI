from app.models.sensor_data import SensorData
from app.repositories.sensor_repository import save_sensor_data, get_all_sensor_data

def create_sensor_data(data):
    if not all(k in data for k in ["device_id", "temperature", "humidity", "status_code", "timestamp"]):
        return None  # Devuelve None si falta algún campo
    
    sensor_data = SensorData(
        device_id=data.get('device_id', 'unknown_device'),
        timestamp=data.get('timestamp', 0),  # Default 0 en caso de error
        temperature=data.get('temperature', 0.0),
        humidity=data.get('humidity', 0.0),
        status_code=data.get('status_code', 200)
    )
    
    save_sensor_data(sensor_data)
    return sensor_data


def retrieve_all_sensor_data():
    return [data.to_dict() for data in get_all_sensor_data()]
