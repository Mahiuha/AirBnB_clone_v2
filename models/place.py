#!/usr/bin/python3
"""Defines the Place class."""
import models
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'), primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """
    Represents a Place for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table places.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """list of Review."""
            lista = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    lista.append(review)
            return lista

        @property
        def amenities(self):
            """list of Review."""
            lista = []
            for review in list(models.storage.all(Amenity).values()):
                if review.place_id == self.id:
                    lista.append(review)
            return lista

        @amenities.setter
        def amenities(self, value):
            if value == Amenity:
                self.amenity_ids.append(value.id)
