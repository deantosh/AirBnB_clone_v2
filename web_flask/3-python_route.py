#!/usr/bin/python3
"""
Script starts a Flask web application.
web application must be listening on 0.0.0.0, port 5000.

Routes:
   /: display “Hello HBNB!”
   /hbnb: display “HBNB”
   /c/<text>: display “C ” followed by the value of the text
              variable (replace underscore _ symbols with a space)
   /python/<text>: display “Python ”, followed by the value of the text
                   variable (replace underscore _ symbols with a space)

Use the option strict_slashes=False
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def display_some_text(text, strict_slashes=False):
    # process text replace _ with " ".
    new_text = text.replace("_", " ")
    result = "C " + new_text
    return result


@app.route("/python/<text>")
def display_python_text(text, strict_slashes=False):
    # replace '_' with ' '
    new_text = text.replace("_", " ")
    # concatenate to form string
    result = "Python " + new_text
    return result


@app.route("/python/")
def python_default_text(strict_slashes=False):
    # pyton default msg when variable is not provided
    return "Python is cool"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
