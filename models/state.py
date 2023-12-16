#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State Class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """
                Getter attribute that returns the list of City instances
                with state_id equals to the current State.id.
            """
            from models import storage
            new_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ 
                Getter attribute that returns the list of City instances
            """
            from models import storage
            new_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
