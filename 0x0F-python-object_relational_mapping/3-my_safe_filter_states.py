#!/usr/bin/python3
"""This script lists all states designated in the command
    safe from sql injection
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8", port=3306)
    cus = db.cursor()
    sql = """SELECT * FROM states WHERE name = %s
          ORDER BY id ASC"""
    cus.execute(sql, (argv[4],))
    row = cus.fetchall()
    for column in row:
        print(column)
    cus.close()
    db.close()
