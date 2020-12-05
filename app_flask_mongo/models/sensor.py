from extensions import db
from datetime import datetime


class Sensor(db.Document):
    model = db.StringField()
    measuring_dimentions = db.ListField()
    description = db.StringField()
