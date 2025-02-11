from flask import Blueprint, request, jsonify
from app.services.sensor_service import create_sensor_data, retrieve_all_sensor_data

sensor_bp = Blueprint('sensor_bp', __name__)

@sensor_bp.route('/', methods=['POST'])
def add_sensor_data():
    data = request.get_json()
    sensor_data = create_sensor_data(data)
    return jsonify({'message': 'Sensor data added', 'id': sensor_data.id}), 201

@sensor_bp.route('/', methods=['GET'])
def get_sensor_data():
    sensor_data_list = retrieve_all_sensor_data()
    result = [
        {
            'id': data.id,
            'device_id': data.device_id,
            'timestamp': data.timestamp,
            'temperature': data.temperature,
            'humidity': data.humidity,
            'status_code': data.status_code
        } for data in sensor_data_list
    ]
    return jsonify(result), 200
