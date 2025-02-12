#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """ return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB! """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_value(text):
    """ display “C ” followed by the value of the text """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
def show_text_value(text):
    """ display “Python ”, followed by the value of the text """
    return f"Python {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
def show_default_text():
    """ display “Python ”, followed by the value of the text """
    return f"Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
