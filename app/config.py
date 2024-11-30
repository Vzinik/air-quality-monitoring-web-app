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
    JWT_SECRET_KEY = "020edb75e072aad4564e404eb4095c94"
    #DATA_ACCESS_URL=os.environ['DATA_ACCESS_URL']