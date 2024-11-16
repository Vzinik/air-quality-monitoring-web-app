from flask import render_template, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from  . import dashboard
from app.dal.user_client import get_device
from app.dal.sensor_client import get_sensor_data


@dashboard.route('/', methods=['GET', 'POST'])
@jwt_required
def home():
    current_user_id = get_jwt_identity()
    devices = get_device(current_user_id)
    return render_template("dashboard.html", devices=devices)


@dashboard.route('/data', methods=['GET'])
def sensor_data():
    device_id = request.args.get('id')
    data = get_sensor_data(device_id)
    return render_template("sensor_readings.html")