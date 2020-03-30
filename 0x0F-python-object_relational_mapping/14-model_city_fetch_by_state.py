#!/usr/bin/python3
"""
prints all the cities from the database
"""
import sqlalchemy
from model_state import State, Base
from model_city import City
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
    for city, state in session.query(City, State).order_by(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()