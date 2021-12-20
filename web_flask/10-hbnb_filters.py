#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask, render_template
from models import storage
from models import State, City, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ States. cities and amenities. """
    states = list(storage.all('State').values())
    states.sort(key=lambda state: state.name)
    cities = list(storage.all('City').values())
    cities.sort(key=lambda city: city.name)
    amenities = list(storage.all('Amenity').values())
    amenities.sort(key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run()
