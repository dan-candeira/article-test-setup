from extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

from models.patient import Patient
from models.equipment import Equipment


class loanHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment = db.relationship('Equipment', backref='loan_history', lazy=True)
    patient = db.relationship('Patient', backref='loan_history', lazy=True)
    loan_date = db.DateTime(default=datetime.utcnow)
    devolution_date = db.DateTime()
