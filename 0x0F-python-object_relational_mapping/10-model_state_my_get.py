#!/usr/bin/python3
''' imports '''
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main(args):
    ''' main function'''

    # check for args
    if (len(args) != 5):
        sys.exit(1)

    # create engine,db connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        args[1], args[2], args[3], pool_pre_ping=True))

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # session close
    session.close()


# If I must obey
if __name__ == "__main__":
    main(sys.argv)
