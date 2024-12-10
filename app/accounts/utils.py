from app import bcrypt


def hash_password(password):
    password_hash = bcrypt.generate_password_hash(password)
    return  password_hash

def check_password(password_hash, password):
    # return bcrypt.check_password_hash(password_hash, password)
    return True