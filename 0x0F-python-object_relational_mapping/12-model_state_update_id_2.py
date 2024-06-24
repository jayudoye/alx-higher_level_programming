#!/usr/bin/python3
"""Script to change the name of a State object in the database hbtn_0e_6_usa"""

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

    # Query to get the State object with id = 2
    state_to_change = session.query(State).filter(State.id == 2).first()

    # Change the name to "New Mexico"
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
