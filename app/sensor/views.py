from flask import request, jsonify

from . import sensor
from app.dal.sensor_client import insert_sensor_data


@sensor.route('/record', methods= ['POST'])
def record():
    device_id = request.args.get('device_id')
    device_token = request.headers.get('device_token')
    data = request.get_json()
    response = insert_sensor_data(device_id, device_token, data)
    return jsonify({"message" : response["message"]}), response["status"]
