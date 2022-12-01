#!/usr/bin/python3
"""script that lists all State objects that contain
 the letter a from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from model_city import City
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
    city = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
    for i in city:
        print("{:s}: ({:d}) {:s}".format(i[0], i[1], i[2]))

    session.close()
