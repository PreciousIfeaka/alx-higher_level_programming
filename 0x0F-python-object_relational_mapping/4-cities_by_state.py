#!/usr/bin/python3
"""This script lists all states and their corresponding cities in the db
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """connect to the database"""
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cus = db.cursor()
    cus.execute("SELECT * FROM states
