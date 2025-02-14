# **nodoESP32WifiTestAPI** - API REST para pruebas con ESP32

API REST desarrollada en **Flask** para la gestión y almacenamiento de datos de 
sensores IoT enviados desde un **nodo IoT basado en ESP32**.  
Sigue una **arquitectura modular y profesional**, incluyendo 
**persistencia en PostgreSQL** y validación de datos con **Marshmallow**.

---

## **Características**
- Desarrollado con **Flask** siguiendo un patrón **modular y profesional**.
- Persistencia en **PostgreSQL**, usando **Flask-SQLAlchemy** y **Alembic** para migraciones.
- Validación de datos con **Marshmallow**, garantizando integridad en los registros.
- Manejo estructurado de errores y logs, con diferentes niveles (`INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- Compatibilidad con el **nodo IoT basado en ESP32**, utilizando **HTTP POST** para el envío de datos.  
  [Repositorio del nodo IoT](https://github.com/asmitmans/nodoESP32Wifi)

---

## Requisitos
Para ejecutar la API, necesitas:

- **Python** (>= 3.10)
- **PostgreSQL** (>= 14)
- **pip** para instalar dependencias

---

## Estructura del Proyecto
El código sigue un diseño modular y organizado:

```
nodoESP32WifiTestAPI/
│── app/
│   ├── controllers/      → Rutas y lógica de API
│   ├── models/           → Definición de modelos SQLAlchemy
│   ├── repositories/     → Acceso a la base de datos
│   ├── schemas/          → Validación de datos con Marshmallow
│   ├── services/         → Lógica de negocio
│   ├── config.py         → Configuración de la aplicación
│   ├── __init__.py       → Inicialización de Flask y BD
│── migrations/           → Migraciones de la base de datos (Alembic)
│── .env                  → Variables de entorno (no subir al repo)
│── requirements.txt      → Dependencias del proyecto
│── README.md             → Documentación
│── run.py                → Punto de entrada de la aplicación
```

---

## Rutas de la API
| Método | Ruta    | Descripción |
|--------|--------|-------------|
| `POST` | `/data` | Recibe datos del sensor y los almacena en la BD |
| `GET`  | `/data` | Obtiene todos los datos almacenados en la BD |

---

## Ejemplo de JSON
El **nodo IoT basado en ESP32** enviará datos en este formato:

```json
{
  "device_id": "esp32-001",
  "timestamp": 1710000000,
  "temperature": 22.5,
  "humidity": 65.3,
  "status_code": 200
}
```

### Códigos de `status_code` definidos:
| Código | Descripción |
|--------|-------------|
| `200`  | Dato correcto recibido y almacenado |
| `300`  | Error en el envío, reintentando desde buffer |
| `500`  | Error en la API |

---

## Cómo ejecutar la API

### Clonar el repositorio
```bash
git clone https://github.com/asmitmans/nodoESP32WifiTestAPI.git
cd nodoESP32WifiTestAPI
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configurar variables de entorno
Antes de ejecutar la API, es necesario configurar las variables de entorno.  

Crea un archivo **.env** en la raíz del proyecto con el siguiente contenido:

```
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_bd
FLASK_APP=app
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=55555
```

- **DATABASE_URL**: URL de conexión a PostgreSQL. Modifica `password` y `nombre_bd` según tu configuración.  
- **FLASK_APP**: Define el módulo principal de la aplicación (`app` en este caso).  
- **FLASK_ENV**: Modo de ejecución (`development` para desarrollo, `production` para producción).  
- **FLASK_RUN_HOST**: Define en qué IP debe correr la API (`0.0.0.0` para hacerla accesible en la red).  
- **FLASK_RUN_PORT**: Puerto en el que se ejecutará la API (`55555` por defecto).  

**Asegúrate de no compartir este archivo `.env` públicamente si contiene credenciales sensibles.**

También es recomendable asegurarse de que `.env` está en el **`.gitignore`** para evitar 
que se suba al repositorio.

### Inicializar la base de datos
```bash
flask db upgrade
```

### Ejecutar la API
```bash
flask run
```

Por defecto, la API estará disponible en:

```
http://127.0.0.1:55555
```

**Si usas otro puerto, revisa la configuración del firewall.**

---

## **Pruebas y Logs**
Para probar la API, usa **cURL** o Postman:

```bash
curl -X POST http://127.0.0.1:55555/data \
     -H "Content-Type: application/json" \
     -d '{"device_id": "esp32-001", "timestamp": 1710000000, "temperature": 22.5, "humidity": 65.3, "status_code": 200}'
```

**Los logs se guardan en `app.log`. Puedes modificar esto en `config.py`.**

---

## **Licencia**
Este proyecto es de **uso libre** bajo la licencia **MIT**.

---

## **Notas finales**
- Revisa el código actualizado en: [nodoESP32WifiTestAPI](https://github.com/asmitmans/nodoESP32WifiTestAPI)
- Si encuentras errores o mejoras, crea un **issue** o **pull request**.

---

## **Resumen de mejoras finales**
- Se parametrizó el puerto con `FLASK_RUN_PORT`.  
- Se añadió advertencia sobre firewall si se usa un puerto diferente.  
- Corrección en compatibilidad, indicando que es para el **nodo IoT** y no directamente ESP32.  
- Corrección en instalación de dependencias, eliminando `venv` innecesario.  
- Explicación más clara de códigos `status_code` en la API.  

---
