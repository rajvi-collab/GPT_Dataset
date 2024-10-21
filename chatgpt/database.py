import os
import sqlite3
import mysql.connector
import psycopg2
from getpass import getpass

def get_database_connection(db_type, host, database, user, password):
    if db_type == "sqlite":
        return sqlite3.connect(database)
    elif db_type == "mysql":
        return mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    elif db_type == "postgresql":
        return psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    else:
        raise ValueError("Unsupported database type")

def backup_database(conn, db_type, backup_file):
    cursor = conn.cursor()
    
    if db_type == "sqlite":
        # SQLite doesn't have a built-in backup command, but you can copy the file
        os.system(f'cp "{conn.database}" "{backup_file}"')
    elif db_type == "mysql":
        cursor.execute(f'SHOW TABLES')
        tables = cursor.fetchall()
        with open(backup_file, 'w') as f:
            for table in tables:
                table_name = table[0]
                cursor.execute(f'SELECT * FROM {table_name}')
                rows = cursor.fetchall()
                for row in rows:
                    f.write(f"{row}\n")
    elif db_type == "postgresql":
        cursor.execute(f'SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\'')
        tables = cursor.fetchall()
        with open(backup_file, 'w') as f:
            for table in tables:
                table_name = table[0]
                cursor.execute(f'SELECT * FROM {table_name}')
                rows = cursor.fetchall()
                for row in rows:
                    f.write(f"{row}\n")
    
    cursor.close()

def main():
    print("Welcome to the Database Backup Script")
    db_type = input("Enter the database type (sqlite/mysql/postgresql): ").strip().lower()

    # Get database credentials and details
    host = input("Enter the database host: ") if db_type in ["mysql", "postgresql"] else None
    database = input("Enter the database name: ")
    user = input("Enter the username: ") if db_type in ["mysql", "postgresql"] else None
    password = getpass("Enter the password: ") if db_type in ["mysql", "postgresql"] else None

    backup_file = input("Enter the backup file path: ")

    try:
        conn = get_database_connection(db_type, host, database, user, password)
        backup_database(conn, db_type, backup_file)
        print(f"Backup successful! Backup saved to: {backup_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()



