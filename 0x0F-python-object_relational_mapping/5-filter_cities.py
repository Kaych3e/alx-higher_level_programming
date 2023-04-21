#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Execution: <mysql username> \
           <mysql password> \
           <database name> \
           <state name searched>
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = " ".join([
        "SELECT cities.name FROM cities",
        "INNER JOIN states ON states.id = cities.state_id",
        "WHERE states.name LIKE BINARY '{}'",
        "ORDER BY cities.id",
    ]).format(sys.argv[4])
    cur.execute(query)
    data = cur.fetchall()
    strdata = ', '.join([i[0] for i in data])
print(strdata)

cur.close()
db.close()
