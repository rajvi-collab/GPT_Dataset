import os
import hashlib
import getpass
import logging



# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentViewer:
    def __init__(self, document_dir, access_control_file):
        """
        Initialnsizes the DocumentViewer.

        Args:
            document_dir (str): Directory containing the documents.
            access_control_file (str): File containing access control rules.
        """
        self.document_dir = document_dir
        self.access_control_file = access_control_file
        self.access_control_rules = self.load_access_control_rules()

    def load_access_control_rules(self):
        rules = {}
        access_control_path = os.path.join(os.path.dirname(__file__), self.access_control_file)
        try:
          with open(access_control_path, 'r') as f:
            for line in f:
                username, file_name = line.strip().split(',')
                if username not in rules:
                    rules[username] = []
                rules[username].append(file_name)
        except FileNotFoundError:
          logger.error(f"Access control file '{self.access_control_file}' not found. Creating a new one.")
        with open(access_control_path, 'w') as f:
            pass  # Create an empty file
        return rules

    def authenticate(self, username, password):
        """
        Authenticates the user.

        Args:
            username (str): Username.
            password (str): Password.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Replace this with your own authentication mechanism
        # For demonstration purposes, we're using a simple hash comparison
        stored_hash = hashlib.sha256("password123".encode()).hexdigest()
        input_hash = hashlib.sha256(password.encode()).hexdigest()
        return stored_hash == input_hash

    def view_document(self, username, file_name):
        """
        Views a document.

        Args:
            username (str): Username.
            file_name (str): File name.

        Returns:
            bool: True if document can be viewed, False otherwise.
        """
        if username in self.access_control_rules and file_name in self.access_control_rules[username]:
            file_path = os.path.join(self.document_dir, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    print(f.read())
                return True
            else:
                logger.error("File not found.")
        else:
            logger.error("Access denied.")
        return False


def main():
    document_dir = "documents"
    access_control_file = "access_control.txt"

    viewer = DocumentViewer(document_dir, access_control_file)

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if viewer.authenticate(username, password):
        logger.info("Authentication successful.")
        file_name = input("Enter file name: ")
        viewer.view_document(username, file_name)
    else:
        logger.error("Authentication failed.")


if __name__ == "__main__":
    main()
 
