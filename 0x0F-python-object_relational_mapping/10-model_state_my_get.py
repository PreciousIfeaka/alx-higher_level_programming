#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """connecting to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_s = session.query(State).all()
    if State is not None:
        for state in state_s:
            if state.name == argv[4]:
                print(state.id)
                break
    if argv[4] != state.name or State is None:
        print("Not found")
    session.close()
