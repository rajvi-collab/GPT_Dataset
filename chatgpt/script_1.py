import os

def create_file(file_name):
    """Creates a new file."""
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created.")
        
def read_file(file_name):
    """Reads and displays content of a file."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Contents of '{file_name}':")
            print(content)
    else:
        print(f"File '{file_name}' does not exist.")
        
def append_to_file(file_name, content):
    """Appends content to a file."""
    with open(file_name, 'a') as file:
        file.write(content + '\n')
        print(f"Appended to '{file_name}': {content}")
        
def delete_file(file_name):
    """Deletes a file."""
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    else:
        print(f"File '{file_name}' does not exist.")

def file_operations():
    """Main function to handle file operations based on user input."""
    while True:
        print("\nFile Operations Menu:")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Append to a file")
        print("4. Delete a file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            file_name = input("Enter the name of the file to create: ")
            create_file(file_name)
            
        elif choice == '2':
            file_name = input("Enter the name of the file to read: ")
            read_file(file_name)
            
        elif choice == '3':
            file_name = input("Enter the name of the file to append to: ")
            content = input("Enter the content to append: ")
            append_to_file(file_name, content)
            
        elif choice == '4':
            file_name = input("Enter the name of the file to delete: ")
            delete_file(file_name)
            
        elif choice == '5':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    file_operations()
