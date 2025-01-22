import mariadb
import sys

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'database': 'POS-Sys'
}

"""
get_connection() function is used to establish a connection to the database.
This function is called in the app.py file to establish a connection to the database.

"""

def get_connection():
    try:
        conn = mariadb.connect(
            user=DB_CONFIG['user'],
            password='',
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database=DB_CONFIG['database']
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)



