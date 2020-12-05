from extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

from models.sensor import Sensor


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp_start = db.DateTime(default=datetime.utcnow)
    timestamp_end = db.DateTime()
    header = db.Column(JSON)
    data_captured = db.Column(JSON)
    collect = db.relationship('Collect', backref='sample', lazy=True)
