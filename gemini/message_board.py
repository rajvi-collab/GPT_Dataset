import datetime

class MessageBoard:
    def __init__(self):
        self.messages = []

    def create_message(self, author, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {
            "author": author,
            "content": content,
            "timestamp": timestamp
        }
        self.messages.append(message)
        print(f"Message created by {author} at {timestamp}.")

    def view_messages(self):
        if not self.messages:
            print("No messages found.")
        else:
            for index, message in enumerate(self.messages):
                print(f"{index + 1}. Author: {message['author']}")
                print(f"   Content: {message['content']}")
                print(f"   Timestamp: {message['timestamp']}")

    def delete_message(self, index):
        if 0 <= index < len(self.messages):
            deleted_message = self.messages.pop(index)
            print(f"Message deleted by {deleted_message['author']} at {deleted_message['timestamp']}.")
        else:
            print("Invalid message index.")

    def edit_message(self, index, new_content):
        if 0 <= index < len(self.messages):
            self.messages[index]["content"] = new_content
            print("Message edited successfully.")
        else:
            print("Invalid message index.")

# Create a message board instance
message_board = MessageBoard()

# Example usage
message_board.create_message("User1", "Hello, world!")
message_board.create_message("User2", "This is another message.")
message_board.view_messages()
message_board.delete_message(1)
message_board.view_messages()
message_board.edit_message(0, "Updated message")
message_board.view_messages()