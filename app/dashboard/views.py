from flask import render_template, request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from  . import dashboard
from app.dal.user_client import get_devices
from app.dal.sensor_client import get_sensor_data


@dashboard.route('/', methods=['GET', 'POST'])
@jwt_required
def home():
    user_id = get_jwt_identity()
    response = get_devices(user_id= user_id)
    if response['status'] == 'success':
        http_response = make_response(render_template("dashboard.html", devices=response["devices"]))
    else:    
        http_response = make_response(render_template("dashboard.html", devices=[]))
    return http_response


@jwt_required
@dashboard.route('/data', methods=['GET'])
def sensor_data():
    # response object structure =
    # {   "data"[{},{},{}], 
    #     "status":"success",
    #     "status code":200
    # }
    user_id = get_jwt_identity()
    device_id = request.args.get('id')
    response = get_sensor_data(user_id, device_id)
    if response['status'] == 'success':
        http_reponse = make_response(render_template("sensor_readings.html", data=response['data']))
        return http_reponse
    else:
        return jsonify({"message": response['status']}), response['status code']