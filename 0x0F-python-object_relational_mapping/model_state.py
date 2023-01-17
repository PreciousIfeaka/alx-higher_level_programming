#!/usr/bin/python3
"""Contains the class definition of a state and a declarative_base instance
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class, inherits from Base instance"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
