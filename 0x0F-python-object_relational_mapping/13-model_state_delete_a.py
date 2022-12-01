#!/usr/bin/python3
"""script that lists all State objects that contain
 the letter a from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib

if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    password = urllib.parse.quote(argv[2])
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query python instances in database
    state = session.query(State).filter(State.name.like('%a%')).all()
    for i in state:
        session.delete(i)

    session.commit()
    session.close()
