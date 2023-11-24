#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import Column, Integer, Float, String, Table, ForeignKey, Base

class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('amenity_id', Integer, ForeignKey('amenities.id')))
