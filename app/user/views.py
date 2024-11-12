from flask import Blueprint,render_template

from app.user.forms import SignupForm, LoginForm
from app import bcrypt

user = Blueprint('user', __name__)

@user.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    return render_template('signup.html', title = 'signup', form = form)

@user.route('/login/', methods = ['GET', 'POST'])
def login():
    return render_template('login.html', title='login')

@user.route('/logout')
def logout():
    return logout