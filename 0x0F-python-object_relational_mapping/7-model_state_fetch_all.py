#!/usr/bin/python3
''' imports'''
import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine, Sequence
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def main(args):
    ''' main function'''

    if (len(args) != 4):
        sys.exit(1)

    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3], pool_pre_ping=True))

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query for allstates
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # session close
    session.close()


# I won't run when I'm imported
if __name__ == "__main__":
    main(sys.argv)
