#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Script argument: <mysql username> \
                 <mysql password> \
                 <database name> \
                 <state name searched>
                 SQL injection free
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `city` \
                 INNER JOIN `states` as `state` \
                    ON `city`.`state_id = `state`.`id` \
                 ORDER BY `city`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
