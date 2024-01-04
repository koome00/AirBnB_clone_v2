#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    update_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("created_at"):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
            if not self.id:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        """from models import storage"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_objs = {}
        tmp_var = self.__dict__

        for key, values in tmp_var.items():
            if '_sa_instance_state' in dict_objs:
                del dict_objs['_sa_instance_state']
            if key == 'created_at' or key == 'updated_at':
                dict_objs[key] = values.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                if not values:
                    pass
                else:
                    dict_objs[key] = values
        
        dict_objs['__class__'] = type(self).__name__
        return dict_objs

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
