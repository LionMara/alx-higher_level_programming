#!/usr/bin/python3
''' modules to be imported'''
import MySQLdb
import sys

def main(args):
    '''main function'''

    # Check if args are enough
    if (len(args) != 5):
        sys.exit(1)

    #store args in variables
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    string_with_state = args[4]

    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=mysql_username,
                                    passwd=mysql_password,
                                    db=database_name)

    #Create a cursor
    cur = db_connection.cursor()

    # split the string_with_state possibly to avoid an injection
    split_list = string_with_state.split(';')

    # query to be used
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY states.id ASC"
    formatted_query = query.format(split_list[0])

    cur.execute(formatted_query)

    # loop through the results
    for row in cur.fetchall():
        print(row)

    #close connections
    cur.close()
    db_connection.close()

# prevents script from running when imported
if __name__ == "__main__":
    main(sys.argv)
