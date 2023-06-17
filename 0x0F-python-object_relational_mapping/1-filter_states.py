#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    csr = db.cursor()
    csr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for state in csr.fetchall():
        print(state)
        csr.close()
        bd.close()
