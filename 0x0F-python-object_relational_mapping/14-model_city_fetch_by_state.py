#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa
"""

import sqlalchemy
from sys import argv
from model_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    State.cities = relationship("City", order_by=City.id,
                                back_populates='state')
    """connecting to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    citie_s = session.query(State, City)\
                     .filter(State.id == City.state_id).all()
    for row in citie_s:
        print("{}: ({}) {})".format(row[0].name, row[1].id, row[1].name))
    session.close()
