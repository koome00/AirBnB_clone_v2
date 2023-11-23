#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import association_table
        name = Column(String(128), nullable=False, default="")

        place_amenities = relationship("Place", secondary=association_table)

    else:
        name = ""