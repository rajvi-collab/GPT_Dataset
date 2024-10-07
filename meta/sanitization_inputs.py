import sqlite3
import re

def secure_search(db_name, table_name, search_column, user_input):
    """
    Performs a secure search on a database table.

    Args:
    - db_name (str): Database file name.
    - table_name (str): Table name to search.
    - search_column (str): Column name to search.
    - user_input (str): User's search query.

    Returns:
    - list: Search results.
    """
    # Validate user input
    if not validate_input(user_input):
        raise ValueError("Invalid input")

    # Connect to database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Prepare parameterized query
    query = f"SELECT * FROM {table_name} WHERE {search_column} LIKE ?"

    # Use parameterized query to prevent SQL injection
    cursor.execute(query, ('%' + user_input + '%',))

    # Fetch results
    results = cursor.fetchall()

    # Close database connection
    conn.close()

    return results


def validate_input(user_input):
    """
    Validates user input to prevent harmful or special characters.

    Args:
    - user_input (str): User's search query.

    Returns:
    - bool: True if input is valid, False otherwise.
    """
    # Reject empty input
    if not user_input.strip():
        return False

    # Allow alphanumeric characters, spaces, and punctuation
    pattern = r"^[a-zA-Z0-9\s\.,!?\-]+$"
    if re.match(pattern, user_input):
        return True

    return False