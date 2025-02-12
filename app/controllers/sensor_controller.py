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
        # Verificar que el Content-Type sea correcto
        if request.content_type != "application/json":
            logger.warning("⚠️ Content-Type incorrecto en la solicitud")
            return jsonify({"error": "El Content-Type debe ser 'application/json'"}), 400

        data = request.get_json()
        validated_data = sensor_schema.load(data)

        # Guardar datos en BD
        sensor_data = create_sensor_data(validated_data)
        logger.info(f"Datos guardados correctamente: {sensor_data.to_dict()}")

        return jsonify(sensor_data.to_dict()), 201

    except ValidationError as e:
        logger.warning(f"Datos inválidos recibidos: {e.messages}")
        return jsonify({"error": "Datos inválidos", "detalles": e.messages}), 400

    except Exception as e:
        if "No se pudo conectar a la base de datos" in str(e):
            logger.error("Fallo crítico: La base de datos no está disponible.")
            return jsonify({"error": "Error interno en el servidor."}), 503  # 503 = Servicio no disponible
        else:
            logger.critical(f"Error inesperado en la API: {e}")
            return jsonify({"error": "Error inesperado en el servidor"}), 500
        
@sensor_bp.route('/data', methods=['GET'])
def get_sensor_data():
    try:
        data = retrieve_all_sensor_data()
        logger.info(f"Consulta de datos - Total registros: {len(data)}")
        return jsonify([d.to_dict() for d in data]), 200

    except SQLAlchemyError as e:
        logger.error(f"Error en la base de datos al consultar datos: {str(e)}")
        return jsonify({"error": "Error interno en el servidor."}), 500

    except Exception as e:
        logger.critical(f"Error inesperado en la API al consultar datos: {str(e)}", exc_info=True)
        return jsonify({"error": "Error inesperado"}), 500
