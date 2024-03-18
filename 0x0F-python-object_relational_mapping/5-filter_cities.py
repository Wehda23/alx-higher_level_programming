#!/usr/bin/python3
"""List of cities and states"""

import MySQLdb
from sys import argv


def main() -> None:
    """Main Function"""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (argv[4],),
    )
    print(", ".join(map(lambda x: x[0], cur.fetchall())))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
