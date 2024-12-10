import requests
from flask import current_app

def get_user(email):
    url = current_app.config['URL_DAL_API']+ f"/{current_app.config['DAL_ROUTE_ACCOUNT']}"
    payload ={'email': email}
    try:
        response = requests.get(url=url, params=payload)
        if response.status_code == requests.codes.ok:
            return {'user': response.json(), 'status':'success', 'status code': response.status_code}
        return {'status': 'failed', 'status code': response.status_code}
    except Exception as e:
        print(f"get_user: {e}") 
        return {'status': 'failed', 'status code': 500}


def create_user(form, hashed_password):
    url = current_app.config['URL_DAL_API']+ f"/{current_app.config['DAL_ROUTE_ACCOUNT']}"
    payload = {
        "first_name": form.first_name.data,
        "last_name": form.last_name.data,
        "email": form.email.data,
        "device_id": form.device_id.data,
        "password": hashed_password 
    }
    try:
        response = requests.post(url=url, json=payload)
        if response.status_code==requests.codes.ok:
            return {'user': response.json(),  'status':'success', 'status code': response.status_code}
        return {'status':'failed', 'status code':response.status_code}
    except Exception as e:
        print(f"create_user: {e}")
        return {'status':'failed', 'status code': 500}
    

def is_user_already_exist(email):
    response = get_user(email=email)
    if response['status']=='success':
        return True
    return False


def get_devices(user_id):
    # fetch devices of a user
    # response object structure =
    # {"devices":[
    #       {"device_id":"","device_name":""},
    #       {"device_id":"","device_name":""}
    # ]}
    url = current_app.config['URL_DAL_API']+ f"/{current_app.config['DAL_ROUTE_DEVICES']}"
    payload = {'id': user_id}    
    try:
        response = requests.get(url=url, params=payload)
        if response.status_code==requests.codes.ok:
            return {'devices': response.json(), 'status': 'success', 'status code': response.status_code}
        return {'status':'failed', 'status code':response.status_code}
    except Exception as e:
        return {'status': 'failed', 'status code':500}