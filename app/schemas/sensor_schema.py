from marshmallow import Schema, fields, ValidationError

class SensorDataSchema(Schema):
    device_id = fields.Str(required=True)
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)
    status_code = fields.Int(required=True)
    timestamp = fields.Int(required=False)
