import getpass
import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Message:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.datetime.now()

class MessageBoard:
    def __init__(self):
        self.users = {}
        self.messages = []

    def create_account(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return
        self.users[username] = User(username, password)
        print("Account created successfully.")

    def login(self, username, password):
        if username not in self.users:
            print("Username does not exist.")
            return
        user = self.users[username]
        if user.password != password:
            print("Incorrect password.")
            return
        print("Logged in successfully.")
        return user

    def post_message(self, user, content):
        self.messages.append(Message(user, content))
        print("Message posted successfully.")

    def view_messages(self):
        for message in self.messages:
            print(f"{message.user.username} at {message.timestamp}:")
            print(message.content)
            print()

def main():
    board = MessageBoard()

    while True:
        print("Message Board Application")
        print("1. Create Account")
        print("2. Login")
        print("3. Post Message")
        print("4. View Messages")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            board.create_account(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = board.login(username, password)
        elif choice == "3":
            if 'user' not in locals():
                print("Please login first.")
                continue
            content = input("Enter message: ")
            board.post_message(user, content)
        elif choice == "4":
            board.view_messages()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()