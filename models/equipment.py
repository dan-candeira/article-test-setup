from extensions import db
from models.sensor import Sensor


class Equipment(db.Document):
    mac_address = db.StringField(primary_key=True)
    name = db.StringField()
    description = db.StringField()
    samppling_frequency = db.IntField()
    sensors = db.ListField(db.ReferenceField('Sensor'), default=list)
    available = db.BooleanField()
