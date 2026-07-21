#!/usr/bin/python3
"""This module provides a script that lists all cities from a MySQL database.

The script joins the cities and states tables from hbtn_0e_4_usa database,
displays the results sorted by city ID, and calls execute exactly once.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Fix: Use single integer indexes to pass pure strings, not slices/lists
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Establish connection to the local MySQL server at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Create a cursor context to handle query string execution
    cursor = db.cursor()

    # Formulate a relational table join query sorted upward by city ID
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)

    # Extract all rows from the pointer and print out each tuple entry
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Terminate the current cursor pipeline and clean up network socket links
    cursor.close()
    db.close()

