from flask import Flask
from flask_bcrypt import Bcrypt

from .config import Config

app=Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)


def create_app():
    return
    app=Flask(__name__)
    app.config.from_object(Config)
      
    
from app.user.views import user
app.register_blueprint(user)

from app.sensor.views import sensor
app.register_blueprint(sensor)

from app.main.views import main
app.register_blueprint(main)