#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':

    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    """ Create cursor object and Execute SQL query to select all states"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    """ print all rows"""
    data = cursor.fetchall()
    for row in data:
        print(row)

    """ Close cursor and database connections"""
    cursor.close()
    db.close()
