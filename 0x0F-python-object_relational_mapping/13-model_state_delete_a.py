#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
Script argument: <mysql username> \
                 <mysql password> \
                 <database name> \
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Create SQLAlchemy engine and session,
    Delete all State objects with a name containing the letter "a"
    Commit the changes and close the session
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
