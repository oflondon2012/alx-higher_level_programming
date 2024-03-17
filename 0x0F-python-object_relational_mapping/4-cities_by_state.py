#!/usr/bin/python3
""" A script that takes in an argument and
    dislays all values in the states table  """


import MySQLdb
from sys import argv


def cities():
    '''function main and its argument'''
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    try:
        db_conn = MySQLdb.connect(host=db_host, port=db_port, user=db_user,
                                  passwd=db_pass, db=db_name, charset="utf8")
        cursor = db_conn .cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities"
        query += " LEFT JOIN states"
        query += " ON cities.state_id=states.id ORDER BY cities.id ASC"
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        db_conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    cities()
