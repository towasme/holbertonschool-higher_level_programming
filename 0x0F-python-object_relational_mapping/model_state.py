#!/usr/bin/python3
"""
class definitions of a state and an base instance
"""


import sys
import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    instance of states class
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name =  Column(String(128), nullable=False)
    