#!/usr/bin/python3
'''
    Define the class City.
'''
from os import getenv
from sqlalchemy import Column, String, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(VARCHAR(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""