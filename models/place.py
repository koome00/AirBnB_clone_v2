#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, VARCHAR
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        city_id = Column(VARCHAR(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(VARCHAR(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''
                Return list: review instances if Review.place_id==curr place.id
                FileStorage relationship between Place and Review
            '''
            list_reviews = []
            for review in models.storage.all("Review").values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            '''
                Return list: amenity inst's if Amenity.place_id=curr place.id
                FileStorage many to many relationship between Place and Amenity
            '''
            return Place.amenity_ids

        @amenities.setter
        def amenities(self, amenity=None):
            '''
                Set list: amenity instances if Amenity.place_id==curr place.id
                Set by adding instance objs to amenity_ids attribute in Place
            '''
            if amenity:
                for amenity in models.storage.all("Amenity").values():
                    if amenity.place_id == self.id:
                        Place.amenity_ids.append(amenity)
