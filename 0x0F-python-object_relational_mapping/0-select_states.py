import MySQLdb
import sys

#Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

#Create cursor object
our = db.cursor()

#Execute SQL query to select all states
our.execute("SELECT * FROM states ORDER BY id ASC")

#print all rows
rows = our fectchall()
for row in rows:
    print(row)

#Close cursor and database connections
our.close()
db.close()
