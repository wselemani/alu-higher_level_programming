#!/usr/bin/python3
"""This module provides a script to filter database states by user input.

The script connects to a local MySQL server and selects states matching a name
provided via a command-line argument, using string formatting for the query.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Step 2: Grab arguments from the command line
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Step 3: Open connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Step 4: Create a cursor to communicate with the DB
    cursor = db.cursor()

    # Step 5: Format the query string with the state name argument
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"\
        .format(state_name)
    cursor.execute(query)

    # Step 6: Fetch all matched entries and print them
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Step 7: Safely close all sessions and connections
    cursor.close()
    db.close()

