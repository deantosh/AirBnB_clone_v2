#!/usr/bin/python3
"""Defines Place class"""

import os
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """creates a place record"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # for db storage
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            'Review', backref='place', cascade='all, delete-orphan')
    else:
        # for file storage
        @property
        def reviews(self):
            """returns: list of reviews instances with
               place_id == Place.id
            """
            # get instance of file storage
            storage = models.storage

            # get all Review objects
            reviews = storage.all(Review)
            review_list = []

            for review in reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list
