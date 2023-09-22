#!/usr/bin/python3
# Displays all values in the states table of database hbtn_0e_0_usa
# Usage: ./my_filter_states.py

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./my_filter_states.py <usr> <pwd> <db> <state_name>")
	sys.exit(1)
    
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db  = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        c.execute("SELECT * FROM states WHERE BINARY name = %s")

	results = c.fetchall()
	for row in results:
	    print(row)
	db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
	sys.exit(1)
        
