#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Column, Integer, String

Base = declarative_base()
class State(BaseModel):
    """ State Class """
    __tablename__ = "state"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete, delete-orphan')
