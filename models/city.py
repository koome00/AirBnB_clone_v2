#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    __tablename__ = 'cities'
    name = column(String(128), nullable=False)
    state_id = column(String(60), nullable=False, ForeignKey('states_id'))
