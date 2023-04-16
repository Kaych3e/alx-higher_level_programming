#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT * FROM cities", "WHERE state_id =
    (SELECT id FROM states WHERE name LIKE %s)", "ORDER BY cities.id",
    state_name = (sys.argv[4],)
    cur.execute(query, state_name)

    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    db.close()
