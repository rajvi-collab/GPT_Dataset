import sqlite3
import re

def search_db(query):
    """
    Function to search a database with sanitized input to prevent SQL injection.
    It assumes an SQLite database, but can be adapted for other SQL-based databases.
    
    Args:
        query (str): The search query input from the user.
    
    Returns:
        list: The results of the search query.
    """
    # Basic input sanitation: Remove any SQL-related characters if they are not needed
    # This example assumes a simple text-based search query.
    
    # Remove any potential harmful SQL characters like ';', '--', etc.
    # Allow only alphanumeric characters and spaces for this example
    sanitized_query = re.sub(r'[^a-zA-Z0-9\s]', '', query)
    
    # Use parameterized queries to further prevent SQL injection
    connection = sqlite3.connect('example.db')  # Connect to your database
    cursor = connection.cursor()
    
    # The SQL query - using a parameterized query (?)
    cursor.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + sanitized_query + '%',))
    
    # Fetch the results
    results = cursor.fetchall()
    
    # Close the connection
    connection.close()
    
    return results

# Example usage (without function execution for now)
# sanitized_results = search_db("some user input")
