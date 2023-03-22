#!/usr/bin/python3
''' Modules to be imported '''
import MySQLdb
import sys


def main(args):
    ''' main function'''

    # Checks if args are 4
    if (len(args) != 5):
        sys.exit(1)

    # Store args in variables.
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    state_name_to_match = args[4]

    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=mysql_username,
                                    passwd=mysql_password,
                                    db=database_name)
    # Create a cursor connection
    cur = db_connection.cursor()

    # SQL query to match passed in state argument
    query = "SELECT * FROM states WHERE BINARY name = '{}'"

    formatted_query = query.format(state_name_to_match)
    # execute the qquery
    cur.execute(formatted_query)

    # loop over the results todisplay
    for row in cur.fetchall():
        print(row)

    # close connections
    cur.close()
    db_connection.close()


# Hey, I won't run if I'm imported
if __name__ == "__main__":
    main(sys.argv)
