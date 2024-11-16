from flask import (render_template,url_for, redirect,
                   flash, make_response)
from app import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token

from . import account
from app.accounts.utils import check_password
from app.dal.user_client import is_user, create_user, get_user
from app.accounts.forms import SignupForm, LoginForm


@account.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if is_user(form.email.data):
            flash("This email is already registered with another account.", "error")
            return render_template(url_for('user.signup'))
        # hash password and put it in form password data#
        user, response = create_user(form)
        if response["status"] != "success":
            flash("An unexpected error occured. Please try again after some time", "error")
            return render_template('signup.html', title = 'signup', form = form)
        flash("Acount created successfully", "success")
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        response = make_response(redirect(url_for('dashboard.home')))
        response.set_cookie('access_token', access_token, httponly=True, secure=True)
        response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True)
        return response
    return render_template('signup.html', title = 'signup', form = form)    


@account.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user and check_password(form.password.data, user.password_hash):
            access_token = create_access_token(identity=form.email.data)
            refresh_token = create_refresh_token(identity=form.email.data)
            response = make_response(redirect(url_for('dashboard.home')))
            response.set_cookie('access_token', access_token, httponly=True, secure=True)
            response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True)
            return response
    else:
        flash("invalid email or password", "error")
    return render_template('login.html', title='login', form=form)


@account.route('/logout')
def logout():
    # logout #
    pass