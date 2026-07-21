#!/usr/bin/python3
"""This module provides a safe database script to filter states by user input.

It uses parameterized arguments to prevent malicious SQL injection attacks
when querying the hbtn_0e_0_usa database for matched state names.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Step 2: Bind database credentials using precise string indexes
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Step 3: Initialize direct engine connection to the local MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_pass,
        db=db_name
    )

    # Step 4: Create execution cursor
    cursor = db.cursor()

    # Step 5: Secure execution using tuple placeholders to prevent injection
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Step 6: Fetch matches and present results directly to stdout
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Step 7: Clear runtime contexts and close connections safely
    cursor.close()
    db.close()

