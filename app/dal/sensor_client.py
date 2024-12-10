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
#     ]
# }
import requests
from flask import current_app

from app.dal.utils import validate_device_user, validate_device_token


def get_sensor_data(user_id, device_id):
    if validate_device_user(user_id, device_id):
        try:    
            url = current_app.config['URL_DAL_API']+F"/{current_app.config['DAL_URL_DEVICES']}"+f"/{device_id}"
            response = requests.get(url=url)
            if response.status_code == requests.codes.ok:       
                return {'data' :response.json(), 'status':'success', 'status code': response.status_code}
        except Exception as e:
            return {'status': 'failed', 'status code': 500}
    return {'status': 'failed', 'status code': 404}


def insert_sensor_data(device_id:str, device_token:str, data:dict):
    if validate_device_token(device_token,device_id):
        try:
            url = current_app.config['URL_DAL_API']+f"/{current_app.config['DAL_URL_DEVICES']}"+f"/{device_id}"
            response = requests.post(url=url, json=data)
            if response.status_code == requests.codes.ok:
                return {'status':'success', 'status code': 200}
        except Exception as e:
            return {'status': 'failed', 'status code': 500}
    return {'status': 'failed', 'status code': 404}