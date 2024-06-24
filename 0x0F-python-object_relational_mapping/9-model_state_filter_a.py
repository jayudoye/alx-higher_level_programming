#!/usr/bin/python3
"""Script to list all State objects containing the letter 'a'
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    # Database connection parameters
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all State objects containing the letter 'a'
    # and order them by id
    states_with_a = (session.query(State)
                     .filter(State.name.like('%a%'))
                     .order_by(State.id)
                     .all())

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
