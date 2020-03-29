#!/usr/bin/python3
"""
script that list all cities from database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    main
    """

    if len(sys.argv) == 4:
        username = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=username, passwd=passwd, db=database)

    cur = db.cursor()
    cur.execute('''SELECT cities.id, cities.name, states.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id ORDER
                 BY cities.id ASC''')

    rows = cur.fetchall()

    for city in rows:
        print(city)
