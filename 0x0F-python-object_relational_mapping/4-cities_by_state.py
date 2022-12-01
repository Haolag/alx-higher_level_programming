#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to database"""
    connet = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             password=argv[2],
                             database=argv[3])
    """create cursor to execute queries using SQL"""
    cursor = connet.cursor()
    query = ("SELECT cities.id, cities.name, states.name FROM states \
                INNER JOIN cities ON states.id = cities.state_id \
                ORDER BY cities.id ASC")
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    connet.close()
