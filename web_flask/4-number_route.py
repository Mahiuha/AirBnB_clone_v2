#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Hello flask. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ HBNB. """
    return "HBNB"


@app.route('/c/<phrase>', strict_slashes=False)
def c(phrase):
    """ Print c phrases. """
    return 'C {}'.format(phrase.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<phrase>', strict_slashes=False)
def python(phrase='is cool'):
    """ Print python phrases, default ('is cool'). """
    return 'Python {}'.format(phrase.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def number(num):
    """ It's a number! """
    if type(num) == int:
        return ("{} is a number".format(num))

if __name__ == '__main__':
    app.run()
