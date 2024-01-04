#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base, BaseModel
import inspect
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None
    classes = {
            "User": User,
            "BaseModel": BaseModel,
            "Place": Place, "State": State,
            "City": City, "Amenity": Amenity,
            "Review": Review
            }

    def __init__(self):
        '''
            Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        '''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Query current database session
        '''
        classes = {
                "User": User,
                "BaseModel": BaseModel,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
        result = {}
        clses = [v for k, v in classes.items() if "BaseModel" not in k]
        if cls is not None:
            if isinstance(cls, str):
                cls = classes[cls]
            clses = [cls]
        for c in clses:
            for instance in self.__session.query(c):
                key = "{}.{}".format(c().__class__.__name__, instance.id)
                result[key] = instance
        return result

    def new(self, obj):
        '''
            Add object to current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit all changes of current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Delete from current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Commit all changes of current database session
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        '''
            Remove private session attribute
        '''
        self.__session.remove()
