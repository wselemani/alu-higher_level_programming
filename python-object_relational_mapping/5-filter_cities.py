#!/usr/bin/python3
"""This module provides a script that lists all cities of a given state.

The script safely handles user inputs using parameterized placeholders to prevent
SQL injection vulnerabilities, fetching results sorted by city ID.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Fix: Ensure strict single integer indexing to pass strings instead of lists
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the local MySQL server at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Establish query execution cursor context
    cursor = db.cursor()

    # Formulate relational query using a safe %s placeholder for parameter
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))

    # Collect matching city names and print joined by a comma and space
    query_rows = cursor.fetchall()
    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))

    # Clean up working cursors and network socket allocations
    cursor.close()
    db.close()

