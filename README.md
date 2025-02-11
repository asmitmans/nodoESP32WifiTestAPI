# **nodoESP32WifiTestAPI** - API REST para pruebas con ESP32

API REST desarrollada en **Flask** para la gestión y almacenamiento de datos de 
sensores IoT enviados desde un **ESP32**. 
Sigue una **arquitectura modular y profesional**, incluyendo 
**persistencia en PostgreSQL** y validación de datos con **Marshmallow**.

---

## Características
- **Desarrollado con Flask** siguiendo un patrón **modular y profesional**.
- **Persistencia en PostgreSQL**, usando **Flask-SQLAlchemy** y **Alembic** para migraciones.  
- **Validación de datos con Marshmallow**, garantizando integridad en los registros.  
- **Manejo estructurado de errores y logs**, con diferentes niveles (`INFO`, `WARNING`, `ERROR`, `CRITICAL`). 
- **Compatibilidad con el nodo IoT basado en ESP32**, utilizando **HTTP POST** para el envío de datos
  [nodo IoT basado en ESP32](https://github.com/asmitmans/nodoESP32Wifi)
---

## Requisitos
Para ejecutar la API, necesitas instalar las siguientes dependencias:

- **Python** (>= 3.10)
- **PostgreSQL** (>= 14)
- **pip** y **venv** para manejar el entorno virtual

Además, se recomienda instalar las dependencias en un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Configuración
### Variables de entorno
Antes de ejecutar la API, configura las credenciales de la base de datos en un 
archivo **`.env`**:

```
DATABASE_URL=postgresql://usuario:password@localhost/nombre_de_tu_bd
```
**No compartas este archivo en el repositorio. Agrega `.env` a `.gitignore`**

---

## **Estructura del Proyecto**
El código sigue un diseño modular y organizado:

```
nodoESP32WifiTestAPI/
│── app/
│   ├── controllers/      # Rutas y lógica de API
│   ├── models/           # Definición de modelos SQLAlchemy
│   ├── repositories/     # Acceso a la base de datos
│   ├── schemas/          # Validación de datos con Marshmallow
│   ├── services/         # Lógica de negocio
│   ├── config.py         # Configuración de la aplicación
│   ├── __init__.py       # Inicialización de Flask y BD
│── migrations/           # Migraciones de la base de datos (Alembic)
│── .env                  # Variables de entorno (no subir al repo)
│── requirements.txt      # Dependencias del proyecto
│── README.md             # Documentación
│── run.py                # Punto de entrada de la aplicación
```

---

## Rutas de la API
| Método | Ruta        | Descripción |
|--------|------------|-------------|
| `POST` | `/data`    | Recibe datos del sensor y los almacena en la BD |
| `GET`  | `/data`    | Obtiene todos los datos almacenados en la BD |

---

## **Ejemplo de JSON**
El **ESP32** enviará datos en este formato:

```json
{
  "device_id": "esp32-001",
  "timestamp": 1710000000,
  "temperature": 22.5,
  "humidity": 65.3,
  "status_code": 200
}
```

### **Códigos de `status_code` definidos:**
| Código | Descripción |
|--------|-------------|
| `200`  | Dato correcto recibido y almacenado |
| `300`  | Error en el envío, reintentando desde buffer |
| `500`  | Error en la API |

---

## Pruebas y Logs
Para probar la API, usa **cURL** o Postman:

```bash
curl -X POST http://127.0.0.1:5000/data \
     -H "Content-Type: application/json" \
     -d '{"device_id": "esp32-001", "timestamp": 1710000000, "temperature": 22.5, "humidity": 65.3, "status_code": 200}'
```

**Logs disponibles** en `app.log` (puedes modificarlo en `config.py`).

---

## **Licencia**
Este proyecto es de **uso libre** bajo la licencia **MIT**.

---

**Notas finales:**  
- Revisa el código actualizado en: [nodoESP32WifiTestAPI](https://github.com/asmitmans/nodoESP32WifiTestAPI)  
- Si encuentras errores o mejoras, crea un **issue** o **pull request**.  

---