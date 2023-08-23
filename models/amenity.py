#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import os
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
