#!/usr/bin/python3
"""
Contains the class definition of a City
Inherits from Base and links to the MySQL table cities
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import delclarative_base

Base = declarative_base()


class City(Base):
    """Class definition of a City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
