#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    query = "SELECT * FROM cities",
    "WHERE state_id=(SELECT id FROM states WHERE name=%s)",
    "ORDER BY cities.id"
    state_name = (sys, argv[4],)
    cursor.execute(query, state_name)

    data = cursor.fetchall()
    for row in data:
        print(row)

    cursor.close()
    db.close()
