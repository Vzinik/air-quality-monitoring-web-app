import os

class Config:
    '''
    #environment variables
    MONGO_USERNAME=os.environ['MONGO_USERNAME']
    MONGO_PASSWORD=os.environ['MONGO_PASSWORD']
    MONGO_PORT=os.environ['MONGO_PORT']
    MONGO_DB=os.environ['MONGO_DB']
    USER_COLLECTION=os.environ['USER_COLLECTION']
    DATA_COLLECTION=os.environ['DATA_COLLECTION']
    MONGO_HOST=os.environ['MONGO_HOST']

    POSTGRES_PASSWORD=os.environ['POSTGRES_PASSWORD']
    POSTGRES_USERNAME=os.environ['POSTGRES_USERNAME']
'''

    MONGO_USERNAME='MONGO_USERNAME'
    MONGO_PASSWORD='MONGO_PASSWORD'
    MONGO_PORT='MONGO_PORT'
    MONGO_DB='MONGO_DB'
    USER_COLLECTION='USER_COLLECTION'
    DATA_COLLECTION='DATA_COLLECTION'
    MONGO_HOST='MONGO_HOST'

    POSTGRES_PASSWORD='POSTGRES_PASSWORD'
    POSTGRES_USERNAME='POSTGRES_USERNAME'
    SECRET_KEY="79f4795a886afd13fe3c0ae3fd6b486a"
    #DATA_ACCESS_URL=os.environ['DATA_ACCESS_URL']

    #dal urls
    URL_SENSOR_DATA="http://192.168.0.106:3000/devices"
    URL_DEVICE="http://192.168.0.106:3000/devices"
    URL_GET_USER="http://192.168.0.106:3000/account"
    URL_CREATE_USER="http://192.168.0.106:3000/account"


    JWT_SECRET_KEY = "020edb75e072aad4564e404eb4095c94"
    JWT_TOKEN_LOCATION = ['cookies']  # Store JWT tokens in cookies
    JWT_COOKIE_SECURE = True  # Secure cookies; requires HTTPS
    JWT_ACCESS_COOKIE_PATH = '/'  # Path for access token cookie
    JWT_REFRESH_COOKIE_PATH = '/refresh'  # Path for refresh token cookie
    JWT_COOKIE_CSRF_PROTECT = False  # Set to True if enabling CSRF protection
    JWT_COOKIE_SAMESITE = 'Strict'  # SameSite policy for cookies