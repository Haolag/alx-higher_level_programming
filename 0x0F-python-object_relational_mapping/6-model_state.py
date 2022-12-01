#!/usr/bin/python3

"""Start link class to table in database 
"""
from sys import argv
from model_state import Base, State
import urllib
from sqlalchemy import (create_engine)
root = argv[1]
#passwd = argv[2]
passwd = urllib.parse.quote(argv[2])
db = argv[3]
if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{root}:{passwd}@localhost/{db}", pool_pre_ping=True)
    #format(argv[1], argv[2], argv[3])
    Base.metadata.create_all(engine)
