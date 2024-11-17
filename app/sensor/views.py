from flask import request, jsonify

from . import sensor
from app.dal.sensor_client import insert_sensor_data

@sensor.route('/record', methods= ['POST'])
def record():
    data = request.get_json()
    if insert_sensor_data(data):
        return jsonify({"status" : "success"})