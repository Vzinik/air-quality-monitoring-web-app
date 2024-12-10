def get_user(email):
    return {'user': {'password': '123456'}, 'message': 'created', 'status' : 'success'}


def create_user(form, password_hash):
    print(form)
    return {'password': '123456','id': 123}, {"message": "created", "status" :" success"}
    

def is_user_already_exist(email):
    user, response = get_user(email=email)
    if user:
        return True
    return False


def get_devices(user_id):
    # fetch devices 
    devices=[{'device_id':'4455'}]
    return devices