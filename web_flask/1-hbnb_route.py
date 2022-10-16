#!/usr/bin/python3
"""
Flask
"""
from flask import Flask

app = Flask(__name__)
def index():
    """'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
