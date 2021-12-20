#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask, render_template
from models import storage
from models import State, City

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Cities inside each state. """
    state = list(storage.all('State').values())
    state.sort(key=lambda state: state.name)
    city = list(storage.all('City').values())
    city.sort(key=lambda city: city.name)
    return render_template('8-cities_by_states.html', list1=state, list2=city)

if __name__ == '__main__':
    app.run()
