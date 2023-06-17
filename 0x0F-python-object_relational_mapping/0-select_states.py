#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
csr = db.cursor()
csr.execute("SELECT * FROM states ORDER BY states.id ASC")
for state in csr.fetchall():
print(state)
csr.close()
bd.close()
