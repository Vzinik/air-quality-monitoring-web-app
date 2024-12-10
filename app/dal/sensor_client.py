# A response object in get_sensor_data looks like this
# response = { 
#     "data":[
#         {
#             "temperature":"",
#             "pressure":"",
#             "humidity":"",
#             "O2":"",
#             "CO2":"",
#             "gas":""
#          },
#          {
#             "temperature":"",
#             "pressure":"",
#             "humidity":"",
#             "O2":"",
#             "CO2":"",
#          },
#     ],
#     "status":{
#         "message" : "",
#         "code": 200
#     }
# }
import requests
from flask import current_app, jsonify

from app.dal.utils import validate_device_user, validate_device_token


def get_sensor_data(user_id, device_id):
    if validate_device_user(user_id, device_id):
        try:    
            url = current_app.config['URL_SENSOR_DATA']+f"/{device_id}"
            response = requests.get(url=url)       
            return response
        except Exception as e:
            return {"data":[], "status":{"message": "Something went wrong", "code": 500}}
    return {"data":[], "status":{"message": "Not found", "code": 404}}


def insert_sensor_data(device_id:str, device_token:str, data:dict):
    if validate_device_token(device_token):
        try:
            url = current_app.config['URL_SENSOR_DATA']+f"/{device_id}"
            response = requests.post(url=url, data =data)
            return response
        except Exception as e:
            return {"message": "Something went wrong", "status": 500}
    return {"message": "Not found","status": 404}