from app import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.BigInteger, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    status_code = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "device_id": self.device_id,
            "timestamp": self.timestamp,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "status_code": self.status_code
        }
