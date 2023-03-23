#!/usr/bin/python3
''' imports'''
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def main(args):
    ''' main function '''

    if (len(args) != 4):
        sys.exit(1)

    # create a db connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        args[1], args[2], args[3], pool_pre_ping=True))

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # session close
    session.close()


# prevents me from running when imported
if __name__ == "__main__":
    main(sys.argv)
