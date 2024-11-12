from flask import Blueprint

sensor = Blueprint('sensor', __name__)

@sensor.route('/record', methods= ['POST'])
def record():
    pass