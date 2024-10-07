import getpass
import json
import datetime

# Define User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Define Message class
class Message:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define Database class
class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = {}
        self.messages = []

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.users = data['users']
                self.messages = data['messages']
        except FileNotFoundError:
            pass

    def save_data(self):
        data = {'users': self.users, 'messages': self.messages}
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def register_user(self, user):
        self.users[user.username] = user.password
        self.save_data()

    def login_user(self, username, password):
        return username in self.users and self.users[username] == password

    def add_message(self, message):
        self.messages.append(message.__dict__)
        self.save_data()

    def get_messages(self):
        return [Message(**msg) for msg in self.messages]


def main():
    db = Database('message_board.db')
    db.load_data()

    while True:
        print("\nMessage Board Application")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = User(username, password)
            db.register_user(user)
            print("User registered successfully!")

        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if db.login_user(username, password):
                print("Login successful!")
                while True:
                    print("\nMessage Board")
                    print("1. Post message")
                    print("2. View messages")
                    print("3. Logout")

                    choice = input("Choose an option: ")

                    if choice == '1':
                        content = input("Enter message: ")
                        message = Message(username, content)
                        db.add_message(message)
                        print("Message posted successfully!")

                    elif choice == '2':
                        messages = db.get_messages()
                        for message in messages:
                            print(f"{message.user} - {message.timestamp}")
                            print(message.content)
                            print()

                    elif choice == '3':
                        break

            else:
                print("Invalid username or password.")

        elif choice == '3':
            break


if __name__ == '__main__':
    main()