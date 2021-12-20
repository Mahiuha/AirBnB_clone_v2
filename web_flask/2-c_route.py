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


if __name__ == '__main__':
    app.run()
