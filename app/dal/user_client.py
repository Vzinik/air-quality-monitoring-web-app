def get_user(email):
    return {"message": "created", "status" :" success"}


def create_user(form, password_hash):
    if form.email.data=="a@a.com":  # Replace with your user creation logic
        return form, {"status": "success", "message": "User created successfully!"}
    else:
        return None, {"status": "failure", "message": "Failed to create user."}


def confirm_account(form):
    user=get_user(form.email.data)
    if user is not None and check_password(form.password.data, user.password):
        return user, {"status": "success", "message": "account found"}
    else:    
        return None, {"status": "failure", "message":"Invalid username or  password"}
    

def is_user(email):
    return False


def check_password(password, password_hash):
    return True


def get_device(user_id):
    # fetch devices 
    devices=[]
    return devices