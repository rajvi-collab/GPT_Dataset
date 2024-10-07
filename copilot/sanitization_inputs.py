import sqlite3

def search_database(user_input):
    # Connect to your database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM your_table WHERE your_column LIKE ?"
    sanitized_input = f"%{user_input}%"
    cursor.execute(query, (sanitized_input,))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the connection
    conn.close()

# Example usage
user_input = input("Enter your search term: ")
search_database(user_input)
