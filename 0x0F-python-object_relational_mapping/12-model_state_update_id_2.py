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
    to_update = session.query(State).filter_by(id=2).first()
    to_update.name = "New Mexico"
    session.commit()
    session.close()
