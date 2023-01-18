#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, insert


if __name__ == "__main__":
    """connecting to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)
    new_state = State(name='Louisiana')
    session.add(new_state)
    all_state = session.query(State).all()
    for place in all_state:
        print("{}: {}".format(place.id, place.name))
    session.close()
