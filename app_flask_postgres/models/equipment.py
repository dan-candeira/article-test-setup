from extensions import db
from sqlalchemy.dialects.postgresql import JSON
from sensor import Sensor


class Equipment(db.Model):
    mac_address = db.Column(db.String(), primary_key=True)
    name = db.Column(db.StringField())
    description = db.Column(db.StringField())
    samppling_frequency = db.Column(db.IntField())
    sensors = db.relationship('Sensor', backref='equipment', lazy=True)
    available = db.Column(db.Boolean(True))
