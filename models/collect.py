from app import db
# from models.sample import Sample
from models.equipment import Equipment
from models.patient import Patient
from datetime import datetime


class Collect(db.Document):
    timestamp_start = db.DateTimeField(default=datetime.utcnow)
    timestamp_end = db.DateTimeField()
    # samples = db.ListField(db.ReferenceField('Sample'), default=list)
    equipment = db.ReferenceField('Equipment')
    patient = db.ReferenceField('Patient')
