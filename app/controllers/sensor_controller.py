import logging
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError  # Captura errores de la base de datos

from app.services.sensor_service import create_sensor_data, retrieve_all_sensor_data
from app.schemas.sensor_schema import SensorDataSchema

sensor_bp = Blueprint('sensor_bp', __name__)
sensor_schema = SensorDataSchema()

# Configurar logs
logger = logging.getLogger(__name__)

@sensor_bp.route('/data', methods=['POST'])
def add_sensor_data():
    try:
        data = request.get_json()
        validated_data = sensor_schema.load(data)

        # Crear y almacenar el dato en la BD
        sensor_data = create_sensor_data(validated_data)
        logger.info(f"Nuevo dato recibido y almacenado: {sensor_data.to_dict()}")

        return jsonify(sensor_data.to_dict()), 201

    except ValidationError as e:
        logger.warning(f"Validación fallida - Datos inválidos: {e.messages}")
        return jsonify({"error": "Datos inválidos", "detalles": e.messages}), 400

    except SQLAlchemyError as e:
        logger.error(f"Error en la base de datos: {str(e)}")
        return jsonify({"error": "Error en la base de datos"}), 500

    except Exception as e:
        logger.critical(f"Error inesperado en la API: {str(e)}", exc_info=True)
        return jsonify({"error": "Error inesperado"}), 500
