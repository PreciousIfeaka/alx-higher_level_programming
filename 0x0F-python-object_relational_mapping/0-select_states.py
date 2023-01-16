#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], database=argv[3], charset="utf8")
    cursor = con.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    if db is not None:
        for row in db:
            print(row)
        cursor.close()
        con.close()
