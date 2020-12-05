from extensions import db

from datetime import datetime

from models.equipment import Equipment
from models.patient import Patient


class LoanHistory(db.Document):
    equipment = db.ReferenceField('Equipment')
    patient = db.ReferenceField('Patient')
    loan_date = db.DateTimeField(default=datetime.utcnow)
    devolution_date = db.DateTimeField()
