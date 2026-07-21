#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up and close connections
    cursor.close()
    db.close()

