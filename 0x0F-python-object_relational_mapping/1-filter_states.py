#!/usr/bin/python3
""" A script that lists all states with a name starting with N (upper N) """


import MySQLdb
from sys import argv


def state():
    '''funtion argument bellow'''
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    try:
        db_conn = MySQLdb.connect(host=db_host, port=db_port, user=db_user,
                passwd=db_pass, db=db_name, charset="utf8")
        cursor = db_conn .cursor()
        query = "SELECT * FROM states WHERE CONVERT(name USING Latin1)"
        query += "COLLATE Latin1_General_CS REGEXP '^N' ORDER BY id ASC"
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db_conn.close()
    except Exception:
        pass

if __name__ == "__main__":
    state()
