from datetime import datetime

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
    
    def login(self, password):
        if self.password == password:
            self.logged_in = True
            print(f"{self.username} logged in successfully.")
        else:
            print("Invalid password.")
    
    def logout(self):
        self.logged_in = False
        print(f"{self.username} logged out.")

# Message class
class Message:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.timestamp = datetime.now()
    
    def display_message(self):
        print(f"[{self.timestamp}] {self.user.username}: {self.content}")

# Thread class
class Thread:
    def __init__(self, title, creator):
        self.title = title
        self.creator = creator
        self.messages = []
    
    def post_message(self, content, user):
        if not user.logged_in:
            print("User must be logged in to post a message.")
            return
        
        new_message = Message(content, user)
        self.messages.append(new_message)
        print(f"Message posted in thread '{self.title}'.")
    
    def display_thread(self):
        print(f"Thread: {self.title} (Created by {self.creator.username})")
        for message in self.messages:
            message.display_message()

# Board class
class Board:
    def __init__(self, name):
        self.name = name
        self.threads = []
    
    def create_thread(self, title, user):
        if not user.logged_in:
            print("User must be logged in to create a thread.")
            return
        
        new_thread = Thread(title, user)
        self.threads.append(new_thread)
        print(f"Thread '{title}' created in board '{self.name}'.")
    
    def display_board(self):
        print(f"Board: {self.name}")
        for thread in self.threads:
            thread.display_thread()

# Main application class
class MessageBoardApplication:
    def __init__(self):
        self.users = []
        self.boards = []
        self.logged_in_user = None
    
    def register_user(self, username, password):
        if self.get_user(username):
            print(f"Username '{username}' is already taken.")
            return
        
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully.")
    
    def login_user(self, username, password):
        user = self.get_user(username)
        if user:
            user.login(password)
            if user.logged_in:
                self.logged_in_user = user
        else:
            print(f"User '{username}' not found.")
    
    def logout_user(self):
        if self.logged_in_user:
            self.logged_in_user.logout()
            self.logged_in_user = None
        else:
            print("No user is currently logged in.")
    
    def create_board(self, board_name):
        if self.logged_in_user:
            new_board = Board(board_name)
            self.boards.append(new_board)
            print(f"Board '{board_name}' created.")
        else:
            print("You must be logged in to create a board.")
    
    def display_boards(self):
        for board in self.boards:
            board.display_board()
    
    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

# Example usage (calls commented out to prevent execution in notebook)
app = MessageBoardApplication()
app.register_user("alice", "password123")
app.register_user("bob", "secret")
app.login_user("alice", "password123")
app.create_board("General Discussion")
app.boards[0].create_thread("Welcome!", app.logged_in_user)
app.boards[0].threads[0].post_message("Hello, everyone!", app.logged_in_user)
app.display_boards()
app.logout_user()
