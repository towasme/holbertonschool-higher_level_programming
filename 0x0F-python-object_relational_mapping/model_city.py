#!/usr/bin/python3
"""
class definitions of City and an base instance
"""
import sys
import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, ForeignKey


Base = declarative_base()


class City(Base):
    """
    instance of citites class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
