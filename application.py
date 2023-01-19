from flask import Flask,request

application=Flask(__name__)

@application.route('/')
def hello_world():
    print(request.method)
    return "<h3>Hello World</h3>"

@application.route('/usuarios/<username>')
def return_username(username):
    return username

@application.post('/')
def hello_world_post():
    print("Hola desde el Post")
    return "Hola"