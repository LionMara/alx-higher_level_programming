#!/usr/bin/python3
''' Modules imported '''
import MySQLdb
import sys


def main(args):
    '''main function'''

    # checks if the args provided are enough
    if len(args) != 4:
        sys.exit(1)

    # the argvs are stored in variables
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]

    # the database connection to db is made
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    # cursor named cur is created to execute MySQL queries
    cur = db.cursor()

    # SQL query to get all states sorted in ascending order
    query = "SELECT * FROM states WHERE name LIKE 'N%'"

    # above query is executed
    cur.execute(query)

    # loop to print the states
    for row in cur.fetchall():
        print(row)

    # cursor connection and database connection are closed
    cur.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv)
