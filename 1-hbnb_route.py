#!/usr/bin/python3
"""
Module contains script to start flask web application
Routes "/" - returns Hello HBNB!
"/hbnb" - returns HBNB
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function that returns HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
