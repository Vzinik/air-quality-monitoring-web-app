from flask import render_template, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from  . import dashboard
from app.dal.user_client import get_devices
from app.dal.sensor_client import get_sensor_data


@dashboard.route('/', methods=['GET', 'POST'])
@jwt_required()
def home():
    current_user_id = get_jwt_identity()
    devices = get_devices(current_user_id)
    #devices= [{'device_id': 123},{'device_id': 123}]
    http_response = make_response(render_template("dashboard.html", devices=devices))
    return http_response


@jwt_required()
@dashboard.route('/data', methods=['GET'])
def sensor_data():
    device_id = request.args.get('id')
    data = get_sensor_data(device_id)
    http_reponse = make_response(render_template("sensor_readings.html", data=data))
    return http_reponse