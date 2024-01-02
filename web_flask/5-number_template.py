#!/usr/bin/python3
"""
Module 5
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
"""

from flask import Flask, render_template

app = Flask(__name__)


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


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    return f"{n:d} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_int(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
