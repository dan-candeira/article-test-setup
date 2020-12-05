from extensions import db
from sqlalchemy.dialects.postgresql import JSON


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String())
    measuring_dimentions = db.Column(JSON)
    description = db.Column(db.String)
