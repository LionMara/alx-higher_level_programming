#!/usr/bin/python3
'''Import modules'''
import MySQLdb
import sys


def main(args):
    ''' main func '''

    # check for args if they are 3
    if (len(args) != 4):
        sys.exit(1)

    db_connection = MySQLdb.connect(host="localhost",
                                    user=args[1],
                                    port=3306,
                                    passwd=args[2],
                                    db=args[3])
    # create cursor
    cur = db_connection.cursor()

    # sql script
    query = "SELECT cities.id, cities.name, states.name\
 FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(query)

    for row in cur.fetchall():
        print(row)
    # close connections
    cur.close()
    db_connection.close()


# Hey, I won't run if imported
if __name__ == "__main__":
    main(sys.argv)
