from extensions import db


class Patient(db.Model):
    cpf = db.Column(db.String(), primary_key=True)
    name = db.Column(db.StringField())
    last_name = db.Column(db.StringField())
    email = db.Column(db.StringField())
    telefone = db.Column(db.StringField())
    lat = db.Column(db.StringField())
    long = db.Column(db.StringField())
