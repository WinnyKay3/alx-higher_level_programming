#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

# Connect database using command-line arguments
my_db = MySQLdb.connect(
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    host=("localhost" if len(argv) < 6 else argv[5]),
)

my_cursor = my_db.cursor()

# Execute a SELECT query to fetch data
my_cursor.execute(
    """
       SELECT * FROM states  WHERE name LIKE BINARY '%{}%'
       ORDER BY states.id ASC
     """.format(
        argv[4]
    )
)
my_data = my_cursor.fetchall()


for row in my_data:
    print(row)
my_cursor.close()
my_db.close()
