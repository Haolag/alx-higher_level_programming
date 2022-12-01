#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connet = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             password=argv[2],
                             database=argv[3])
    cursor = connet.cursor()
    query = "SELECT cities.name FROM states INNER JOIN cities ON \
                states.id = cities.state_id WHERE states.name=%s \
                ORDER BY cities.id ASC"
    cursor.execute(query, (argv[4],))
    records = cursor.fetchall()
    print(', '.join(["{:s}".format(city[0]) for city in records]))
    cursor.close()
    connet.close()
