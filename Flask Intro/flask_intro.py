from flask import Flask
from flask import request
from operations import add, sub, multi, div

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return '<h1>Welcome</h1>'

@app.route('/welcome/home')
def welcome_home():
    return '<h1>welcome home!</h1>'

@app.route ('/welcome back')
def welcome_back():
    return "<h1>welcome back!</h1>"

@app.route ('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return f"{a} + {b} = {a+b}"

@app.route ('/sub')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return f"{a} - {b} = {a-b}"

@app.route ('/multi')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return f"{a} x {b} = {a*b}"

@app.route ('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return f"{a} / {b} = {a/b}"


arguments = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<arg>')
def math_args(arg):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"{a} {arg} {b} = {arg(a,b)}"
