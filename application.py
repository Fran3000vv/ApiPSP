from flask import Flask

application=Flask(__name__)

@application.route('/')
def hello_world():
    return "<h3>Hello World</h3>"

@application.route('/usuarios/<username>')
def return_username(username):
    return username