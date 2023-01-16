#!/usr/bin/python3
"""This script lists all states designated in the command
    safe from sql injection
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cus = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE '{:s}'".format(argv[4])
    cus.execute(sql)
    row = cus.fetchall()
    if row is not None:
        for column in row:
            if column[1] == argv[4]:
                print(column)
        cus.close()
        db.close()
