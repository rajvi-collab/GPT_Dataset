class MessageBoard:
    def __init__(self):
        self.messages = []

    def post_message(self, username, message):
        if username and message:
            self.messages.append({'username': username, 'message': message})

    def display_messages(self):
        if not self.messages:
            print("No messages yet.")
        else:
            for msg in self.messages:
                print(f"{msg['username']}: {msg['message']}")

def main():
    board = MessageBoard()
    while True:
        print("\nMessage Board")
        print("1. Post a message")
        print("2. View messages")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter your name: ")
            message = input("Enter your message: ")
            board.post_message(username, message)
        elif choice == '2':
            board.display_messages()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
