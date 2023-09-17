#!/usr/bin/python3
"""Lists all states with name starting with N from hbtn_0e_0_usa.
usage: ./filter_states.py"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host=("localhost" if len(sys.argv) < 5 else sys.argv[4]),
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
