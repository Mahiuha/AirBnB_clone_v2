#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
import os

if (os.getenv("HBNB_TYPE_STORAGE") == "db"):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # FileStorage() = [Place] (861cb0ed-d4e2-4258-b8cc-e9893d264434)
    #  {'id': '861cb0ed-d4e2-4258-b8cc-e9893d264434',
    #  'created_at': datetime.datetime(2020, 12, 16, 17, 10, 26, 302193),
    #  'updated_at': datetime.datetime(2020, 12, 16, 17, 10, 26, 302258),
    #  'city_id': '0001', 'user_id': '0001', 'name': 'My little house',
    #  'number_rooms': '4', 'number_bathrooms': '2', 'max_guest': '10',
    #  'price_by_night': '300', 'latitude': '37.773972',
    #  'longitude': '-122.431297'}
    storage = FileStorage()
storage.reload()
