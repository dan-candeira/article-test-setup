from extensions import db


class Patient(db.Document):
    cpf = db.StringField(primary_key=True)
    birth_date = db.DateTimeField()
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField()
    phone = db.StringField()
    address = db.StringField()
    lat = db.StringField()
    long = db.StringField()
