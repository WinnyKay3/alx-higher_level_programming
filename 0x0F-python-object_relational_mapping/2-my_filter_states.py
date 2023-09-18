#!/usr/bin/python3
# Displays all values in the states table of database hbtn_0e_0_usa
# Usage: ./my_filter_states.py

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    host=("localhost" if len(sys.argv) < 5 else sys.argv[4]),	
    c = db.cursor()
    c.execute(
        "SELECT * \
	         FROM `states` \
		 WHERE BINARY `name` = '{}'".format(
            sys.argv[4]
        )
    )
    [print(state) for state in c.fetchall()]
