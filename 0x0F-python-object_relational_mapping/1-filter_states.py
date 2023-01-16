#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
            "SELECT id, name FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    db = cursor.fetchall()
    if db is not None:
        for row in db:
            print("({}, '{}')".format(row[0], row[1]))
        cursor.close()
        con.close()
