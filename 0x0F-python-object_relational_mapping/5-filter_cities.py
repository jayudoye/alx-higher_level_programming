#!/usr/bin/python3
"""This module  lists all cities from the database hbtn_0e_0_usa"""
import sys

import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sname = sys.argv[4]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         password=password, db=database, charset='utf8')
    cr = db.cursor()
    query = """SELECT ct.id, ct.name FROM cities ct LEFT JOIN
    states st ON st.id = ct.state_id WHERE st.name=%s  ORDER BY ct.id ASC"""
    cr.execute(query, (sname,))
    print(', '.join([rec[1] for rec in cr.fetchall()]))
    cr.close()
    db.close()
