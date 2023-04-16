#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
 Should be safe from MySQL injections!"""
 import MySQLdb
 import sys

 if __name__ == '__main__':
     username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
     db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
     cursor = db.cursor()
     query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
     cursor.execute(query, (state_name,))
     data = cursor.fetchall()
     for row in data:
         print(row)

    cursor.close()    
    db.close()
