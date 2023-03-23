#!/usr/bin/python3
'''Modules to be imported'''
import MySQLdb
import sys


def main(args):
    '''main function'''

    # check if passedargs are as needed
    if (len(args) != 5):
        print("checknumber of args")
        sys.exit(1)

    # create a database connection
    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=args[1],
                                    passwd=args[2],
                                    db=args[3])

    # create a cursor
    cur = db_connection.cursor()

    # sql query
    query = "SELECT cities.name FROM cities JOIN states ON\
 cities.state_id = states.id WHERE states.name = '{}' ORDER BY cities.id ASC"

    formatted = query.format(args[4])

    # execute the query
    cur.execute(formatted)

    # loop todisplay results
    print(", ".join(row[0] for row in cur.fetchall()))

    # close connections
    cur.close()
    db_connection.close()


# Hey, I won't run when I'mimported
if __name__ == "__main__":
    main(sys.argv)
