#!/usr/bin/python3

"""
    script that list state object from the
    database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def state():
    """Class function """
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    engine = create_engine(
             'mysql+mysqldb://{}:{}@{}/{}'
             .format(db_user, db_pass, db_host, db_name),
             pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    state()
