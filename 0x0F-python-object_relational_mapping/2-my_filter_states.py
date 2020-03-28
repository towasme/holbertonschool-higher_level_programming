#!/usr/bin/python3
"""
script that list all states starting with N from database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    main
    """

    if len(sys.argv) == 5:
        username = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]
        argument = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username, passwd=passwd, db=database)

    cur = db.cursor()
    cur.execute('''SELECT * FROM states
                 WHERE name='{}' ORDER BY id ASC'''.format(argument))

    rows = cur.fetchall()

    for state in rows:
        print(state)
