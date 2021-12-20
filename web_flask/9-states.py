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


@app.route('/states', strict_slashes=False)
@app.route('/states/<_id>', strict_slashes=False)
def cities_by_states(_id=None):
    """ Cities inside each state. """
    states = list(storage.all('State').values())
    states.sort(key=lambda state: state.name)
    cities = list(storage.all('City').values())
    cities.sort(key=lambda city: city.name)

    state_name = None
    for state in states:
        if state.id == _id:
            state_name = state.name
    return render_template('9-states.html', states=states, cities=cities,
                           _id=_id, state_name=state_name)


if __name__ == '__main__':
    app.run()
