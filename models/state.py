#!/usr/bin/python3
"""Defines a State class"""

from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """creates the state record"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade="all, delete-orphan")

    @property
    def cities(self):
        """returns list of City instances with state_id ==
           current state_id.
           This estabishes the FileStorage relationship between
           State and City.
        """
        city_list = []
        for city_obj in models.storage.all(City).values():
            if city_obj.state_id == self.id:
                city_list.append(city)
        return city_list
