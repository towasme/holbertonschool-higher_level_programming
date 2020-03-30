#!/usr/bin/python3
"""
script to update a state to the state table
"""
import sqlalchemy
from model_state import State, Base
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter_by(id=2).first()
    update_state.name = 'New Mexico'
    session.commit()
