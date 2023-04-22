#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
Script argument: <mysql username> \
                 <mysql password> \
                 <database name> \
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    Get the arguments, Create the SQLAlchemy engine and session
    Query database for all City objects and print them
    Close the session
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))

    session.close()
