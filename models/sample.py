from extensions import db
from models.collect import Collect
from datetime import datetime


class Sample(db.Document):
    timestamp_start = db.DateTimeField(default=datetime.utcnow)
    timestamp_end = db.DateTimeField()
    header = db.ListField(default=list)
    data_captured = db.DynamicField()
    collect = db.ReferenceField('Collect')
