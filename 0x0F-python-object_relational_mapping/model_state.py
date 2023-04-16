#!/usr/bin/python3
"""
Python file that contains the class definition of a State
and an instance Base = declarative_base().
State class inherits from Base tips, links to MySQL table states
"""

from sqlalchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()

"""State class inheriting from base.
tablename: name of table in database
id: column of unique integer that is a primary key and not null
name: column of string with 128 char max and is not null
"""


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
