#!/usr/bin/python3
"""
This module takes in an argument and displays all values in the `states` table
of `hbtn_0e_0_usa` where `name` matches the argument
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like '{:s}'".format(argv[4]))
    """Executes the cursor object"""
    row = cur.fetchall()
    if row is not None:
        for column in row:
            if column[1] == argv[4]:
                print(column)

        """Closing cursor and database connection"""
        cur.close()
        db.close()
