import argparse
import mysql.connector
from mysql.connector import errorcode
import os
import datetime

# Define database connection function
def connect_to_db(host, username, password, database):
    """Establish a connection to the MySQL database."""
    try:
        cnx = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None

# Define database backup function
def backup_database(cnx, database, backup_path):
    """Backup the MySQL database to a file."""
    cursor = cnx.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    backup_file = os.path.join(backup_path, f"{database}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql")

    with open(backup_file, 'w') as f:
        for table in tables:
            cursor.execute(f"SHOW CREATE TABLE {table[0]}")
            create_table = cursor.fetchone()
            f.write(create_table[1] + ";\n\n")

            cursor.execute(f"SELECT * FROM {table[0]}")
            rows = cursor.fetchall()
            for row in rows:
                f.write(f"INSERT INTO {table[0]} VALUES ({', '.join(['%s'] * len(row))});\n" % row)

    print(f"Database backed up to {backup_file}")

# Parse user input
parser = argparse.ArgumentParser(description='MySQL Database Backup Script')
parser.add_argument('--host', required=True, help='Database host')
parser.add_argument('--username', required=True, help='Database username')
parser.add_argument('--password', required=True, help='Database password')
parser.add_argument('--database', required=True, help='Database name')
parser.add_argument('--backup-path', required=True, help='Backup file path')

args = parser.parse_args()

# Establish database connection
cnx = connect_to_db(args.host, args.username, args.password, args.database)

if cnx:
    # Perform database backup
    backup_database(cnx, args.database, args.backup_path)
    cnx.close()