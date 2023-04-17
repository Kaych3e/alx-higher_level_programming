#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Creates the engine that connects to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    """Create a session to communicate with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database for the first state"""
    state = session.query(State).order_by(State.id).first()

    """If the table is empty, print 'Nothing'"""
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
