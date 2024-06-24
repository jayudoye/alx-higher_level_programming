#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa"""

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

    # Create the State "California" with the City "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])

    # Add the State object to the session and commit to the database
    session.add(california)
    session.commit()

    # Close the session
    session.close()
