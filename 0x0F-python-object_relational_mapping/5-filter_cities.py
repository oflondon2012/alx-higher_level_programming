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
    search_arg = argv[4]
    db_host = "localhost"
    db_port = 3306
    try:
        db_conn = MySQLdb.connect(host=db_host, port=db_port, user=db_user,
                                  passwd=db_pass, db=db_name, charset="utf8")
        cursor = db_conn .cursor()
        query = "SELECT cities.name FROM cities INNER JOIN states"
        query += " ON cities.state_id = states.id WHERE states.name = %s"
        query += " ORDER BY cities.id ASC"
        cursor.execute(query, (search_arg, ))
        cities = cursor.fetchall()
        rlist = []
        for city in cities:
            rlist.append(city[0])
        print(", ".join(rlist))
        cursor.close()
        db_conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    cities()
