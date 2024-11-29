# handles routes for signup, login and logout
# --signup--
# get method - return signup page
# post method - calls create_user(form, hashed_password) 
# 
# --login--
# get method - return login page
# post method - calls get_user which returns user object and dal_response which contains a status and a message
# 
# --logout--
# removes the hwt

from flask import (render_template,url_for, redirect,
                   flash, make_response)
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                jwt_required, get_jwt)

from . import account
from app.accounts.utils import check_password, hash_password
from app.dal.user_client import is_user_already, create_user, get_user
from app.accounts.forms import SignupForm, LoginForm


@account.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if is_user_already(form.email.data):
            flash("This email is already registered with another account.", "error")
            http_response = make_response(render_template(url_for('user.signup')))
            http_response.status_code = 200
            return http_response
        hash = hash_password(form.password.data)
        user, dal_response = create_user(form, hash)
        if dal_response["status"] != "success":
            flash("An unexpected error occured. Please try again after some time", "error")
            http_response = make_response(render_template('signup.html', title = 'signup', form = form))
            http_response.status_code = 200
            return http_response
        flash("Account created successfully", "success")
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        http_response = make_response(redirect(url_for('dashboard.home')))
        http_response.set_cookie('access_token', access_token, httponly=True, secure=True)
        http_response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True)
        return http_response
    http_response = make_response(render_template('signup.html', title = 'signup', form = form))    


@account.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user, dal_response = get_user(form.email.data)
        if dal_response["status"] != "success":
            flash("An unexpected error occured. Please try again after some time", "error")
            http_response = make_response(render_template('login.html', title = 'register', form = form))
            return http_response
        if user and check_password(user.password_hash, form.password.data):
            access_token = create_access_token(identity=form.email.data)
            refresh_token = create_refresh_token(identity=form.email.data)
            http_response = make_response(redirect(url_for('dashboard.home')))
            http_response.set_cookie('access_token', access_token, httponly=True, secure=True)
            http_response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True)
            return http_response
    else:
        flash("invalid email or password", "error")
    http_response = make_response(render_template('login.html', title='register', form=form))
    return http_response


@account.route('/logout')
@jwt_required
def logout():
    jti = get_jwt()["jti"]
    http_response = make_response(url_for('main.home'))
    http_response.set_cookie('access_token', '', httponly=True, secure=True)
    http_response.set_cookie('refresh_token', '', httponly=True, secure=True)
    return http_response