#!/usr/bin/python3
import MySQLdb
import sys
"""
script that list all states from database
"""

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
cur.execute('SELECT * FROM states ORDER BY states.id ASC')

rows = cur.fetchall()

for state in rows:
        print(state)
