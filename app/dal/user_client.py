def get_user(email):
    return user, {"message": "created", "status" :" success"}


def create_user(form, password_hash):
    pass
    

def is_user_already_exist(email):
    user, response = get_user(email=email)
    if user:
        return True
    return False


def get_devices(user_id):
    # fetch devices 
    devices=[]
    return devices