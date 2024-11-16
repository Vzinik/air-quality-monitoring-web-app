from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from .config import Config


bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app=Flask(__name__)
    
    app.config.from_object(Config)
    bcrypt.init_app(app)
    jwt.init_app(app)

    #routes
    from app.accounts import account
    app.register_blueprint(account, url_prefix='/account')

    from app.sensor import sensor
    app.register_blueprint(sensor, url_prefix='/sensor')

    from app.main import main
    app.register_blueprint(main)

    from app.dashboard import dashboard
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    return app