"""
This module contains common functions and utilities used across the application.
"""

import psycopg2

# Connect to your PostgreSQL database
def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        psycopg2.extensions.connection: A connection object to the PostgreSQL database.
    """
    conn = psycopg2.connect(
        "dbname=test user=user password=password host=localhost port=5432"
    )
    return conn
