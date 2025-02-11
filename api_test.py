from flask import Flask, request, jsonify, Blueprint

# Definir el Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Datos recibidos:", data)
    return jsonify({"status": "OK"}), 200

# Configurar la app principal
app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55555)
