#!/usr/bin/python3
"""
script to list all State objects from database
"""
import sqlalchemy
from model_state import State, Base
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import re

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id) \
                        .filter(State.name.like(sys.argv[4])):
        print("{}".format(state.id))
    session.close()
