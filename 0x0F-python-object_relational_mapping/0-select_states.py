#!/usr/bin/python3
"""Script that lists states from database"""
import MySQLdb
from sys import argv


def main() -> None:
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Create cursor
    cur = db.cursor()
    # Execute command
    cur.execute("SELECT * FROM states")
    # grab data
    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Close connection
    cur.close()
    db.close()

if __name__ == '__main__':
    main()