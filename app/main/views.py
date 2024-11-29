from flask import render_template, make_response

from . import main

@main.route('/')
def home():
    http_response = make_response(render_template('home.html', title= 'home'))