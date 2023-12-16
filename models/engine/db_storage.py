#!/usr/bin/python3
"""
    Class DBStorage
"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

HBNB_MYSQL_USER = "hbnb_dev"
HBNB_MYSQL_PWD = "hbnb_dev_pwd"
HBNB_MYSQL_HOST = "localhost"
HBNB_MYSQL_DB = "hbnb_dev_db"


class DBStorage():
    """ This class manages the storage of the  data """

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes a new instance of DBStorage. """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            BaseModel.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Returns a dictionary with all objects in the database.
            If cls is specified, returns only objects of that class.
        """
        dict_cls = {}
        if cls is None:
            for cls_name in self.classes:
                obj_class = self.classes[cls_name]
                objs = self.__session.query(obj_class).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dict_cls[key] = obj
        else:
            for k, v in self.classes.items():
                if k == cls:
                    cls = v
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                dict_cls[key] = obj
        return dict_cls

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload the database and create a new session. """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """  """
        self.__session.close()
