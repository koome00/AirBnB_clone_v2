#!/usr/bin/python3
"""
Module 3 
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    if '_' in text:
        message = text.replace('_', ' ')
    else:
        message = text
    return 'C' + ' ' + message


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    if '_' in text:
        message = text.replace('_', ' ')
    else:
        message = text
    return 'Python' + ' ' + message


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
