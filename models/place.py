#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column((Integer), nullable=False, default=0)
    number_bathrooms = Column((Integer), nullable=False, default=0)
    max_guest = Column((Integer), nullable=False, default=0)
    price_by_night = Column((Integer), nullable=False, default=0)
    latitude = Column((Float), nullable=True)
    longitude = Column((Float), nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade='all, delete, delete-orphan')
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=True)

    @property
    def reviews(self):
        """
            Getter attribute reviews that returns the
            list of Review instances.
        """
        from models import storage
        new_list = []
        for value in storage.all(Review).values():
            if value.place_id == self.id:
                new_list.append(value)
        return new_list

    @property
    def amenities(self):
        """
            Getter attribute amenities that returns the
            list of Amenity instances.
        """
        from models import storage
        new_list = []
        for value in storage.all(Amenity).values():
            if value.amenity_ids == self.id:
                new_list.append(value)
        return new_list

    @amenities.setter
    def amenities(self, value):
        """
            Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids.
        """
        if type(value) is Amenity:
            self.amenity_ids.append(value.id)
