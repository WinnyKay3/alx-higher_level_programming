#!/usr/bin/python3
#lists all states from the database hbtn_0e_0_usa
#should take 3 arguments:mysql username, mysql password and database name (no argument validation needed).
import sys
import MySQLdb

if __name__ == "__main__":
	db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	c = db.cursor ()
	c.execute("SELECT * FROM `states`")
	[print(state) for state in c.fetchall()]