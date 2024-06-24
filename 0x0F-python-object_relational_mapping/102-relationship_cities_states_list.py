#!/usr/bin/python3
"""Script to list all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':

    # Database connection parameters
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all City objects and their associated
    # State objects using .state
    cities = (session.query(City)
              .order_by(City.id)
              .all())

    # Print the results
    for city in cities:
        state_name = city.state.name if city.state else None
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    # Close the session
    session.close()
