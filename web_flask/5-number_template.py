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
   /number/<n>: display “n is a number” only if n is an integer
   /number_template/<n>: display a HTML page only if n is an integer:
         - H1 tag: “Number: n” inside the tag BODY

Use the option strict_slashes=False
"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>")
def display_number(n, strict_slashes=False):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/python/")
def python_default_text(strict_slashes=False):
    # pyton default msg when variable is not provided
    return "Python is cool"


@app.route("/number_template/<int:n>")
def display_page(n, strict_slashes=False):
    # if n is integer display page
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
