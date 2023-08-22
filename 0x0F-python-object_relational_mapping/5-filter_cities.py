#!/usr/bin/python3
<<<<<<< HEAD
"""Script that takes in name of state as an argument and lists all cities 
of that state using the database hbtn_0e_4_usa."""
=======
'''Script that takes in name of state as an argument and lists all cities 
of that state using the database hbtn_0e_4_usa'''
>>>>>>> 194ce989afea6fdb3b75c4af7935900a4511338c

import MySQLdb
from sys import argv

if __name__ == "__main__":
<<<<<<< HEAD
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name LIKE %(state_name)s\
    ORDER BY cities.id ASC",
        {"state_name": argv[4]},
    )
    res = cur.fetchall()
    print(", ".join(row[0] for row in res))
    db.close()
=======
     db = MySQLdb.connect(host="localhost",
		         port=3306,
			 user=argv[1],
			 passwd=argv[2],
			 database=argv[3])
     cur = db.cursor()
     cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
	cities.state_id = states.id WHERE states.name LIKE %(state_name)s\
	ORDER BY cities.id ASC", {'state_name': argv[4]})
        res = cur.fetchall()
	print(', '.join(row[0] for row in res))
	db.close()
>>>>>>> 194ce989afea6fdb3b75c4af7935900a4511338c
