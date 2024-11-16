from flask import Blueprint

account = Blueprint('user', __name__)

from . import views
