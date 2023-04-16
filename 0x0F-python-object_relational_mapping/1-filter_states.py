#!/usr/bin/python
"""script that lists all states with a name starting with N
    from the database hbtn_0e_0_usa"""
import MySqldb
import sys

if __name__ == '__main__':

""" Connect to MySQL server and create cursor object"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], 
                        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    our = db.cursor()

    our.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = our.fetchall()
    for row in data:
        print(row)

    our.close()
    db.close()
