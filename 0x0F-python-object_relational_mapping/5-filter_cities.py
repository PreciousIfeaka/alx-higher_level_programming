#!/usr/bin/python3
"""Lists all cities of the state given in the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cur = db.cursor()  # creating a cursor object for db
    sql = """SELECT cities.name, states.name
             FROM cities INNER JOIN states
             ON states.id = cities.state_id
             WHERE states.name = '{:s}'""".format(argv[4])
    cur.execute(sql)
    cities = cur.fetchall()
    citylist = []
    for city in cities:
        citylist.append(city[0])
    if len(citylist) == 0:
        print()
    for place in citylist:
        if place == citylist[-1]:
            print(place)
        else:
            print(place, end=", ")
    cur.close()
    db.close()
