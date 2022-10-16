#!/usr/bin/python3
"""
Flask
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """'HBNB'"""
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """C followed by the value of text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Python folled by the value of text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """n is a number"""
    try:
        n = int(n)
        return "{} is a number".format(n)
    except:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

