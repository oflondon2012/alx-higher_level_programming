#!/usr/bin/python3

"""
    script that list state object from the
    database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def state():
    """Class function """
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    try:
        engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(db_user, db_pass, db_host, db_name),
                pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).filter(State.name.like("%a%")).order_by(
                 State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    state()
