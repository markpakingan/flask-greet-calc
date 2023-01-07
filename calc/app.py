# Put your app in here.


# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
#     Adds a and b and returns result as the body.
# /sub
#     Same, subtracting b from a.
# /mult
#     Same, multiplying a and b.
# /div
#     Same, dividing a by b.

# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask (__name__)

# @app.route('/')
# def welcome():
#     return "testing"

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

operations = {
    "add" : add, 
    "sub" : sub, 
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def do_math(oper):


    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = operations[oper](a,b)

    return str(result)


