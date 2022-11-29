#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
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
    select_query = ("SELECT * FROM states ORDER BY id ASC")
    cursor.execute(select_query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    connet.close()
