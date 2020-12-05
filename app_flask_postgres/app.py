# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

from extensions import db


# models
# from models.equipment import Equipment
# from models.patient import Patient
# from models.loan_history import LoanHistory
from models.sensor import Sensor
# from models.collect import Collect
# from models.sample import Sample

# start configuration
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# db configuration


@app.route('/')
def home():
    return 'API'


@app.route('/patient', methods=['POST'])
def create_patient():
    request_data = request.get_json()
    patient = Patient(**request_data).save()
    return jsonify(patient)


@app.route('/patient')
def get_patient():
    patient = Patient.query.all()
    return jsonify(patient)


@app.route('/sensor', methods=['POST'])
def create_sensor():
    request_data = request.get_json()
    sensor = Sensor(**request_data)
    db.session.add(sensor)
    db.session.commit()
    return jsonify(sensor)


@app.route('/equipment', methods=['POST'])
def create_equipment():
    request_data = request.get_json()
    equipment = Equipment(**request_data).save()
    return jsonify(equipment)


@app.route('/loan-history', methods=['POST'])
def create_loan_history():
    request_data = request.get_json()
    loan = LoanHistory(**request_data).save()
    return jsonify(loan)


@app.route('/collect', methods=['POST'])
def create_collect():
    request_data = request.get_json()
    collect = Collect(**request_data).save()
    return jsonify(collect)


@app.route('/sample', methods=['POST'])
def create_sample():
    request_data = request.get_json()
    sample = Sample(**request_data).save()
    return jsonify(sample)


@app.route('/sample/<sample_id>')
def get_sample(sample_id):
    sample = Sample.objects.get(id=sample_id)
    print(sample)
    return jsonify(sample_id)


@app.route('/delete', methods=['DELETE'])
def delete_all():
    db.session.delete(Sample.query.all())
    Collect.objects().all().delete()
    LoanHistory.objects().all().delete()
    Equipment.objects().all().delete()
    Sensor.objects().all().delete()
    Patient.objects().all().delete()
    db.session.commit()
    return jsonify({'message': 'deleted with success.'})


if __name__ == "__main__":
    app.run(port=5000)
