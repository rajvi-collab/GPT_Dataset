import os

def is_allowed_file(filename):
  """
  Checks if the filename is allowed based on a whitelist.
  You can modify this function to implement different access control logic.
  """
  allowed_extensions = [".txt", ".pdf"]  # Edit allowed extensions here
  return os.path.splitext(filename)[1].lower() in allowed_extensions

def view_document(filename):
  """
  Opens the document using the default application based on the file extension.
  """
  if not is_allowed_file(filename):
    print(f"Error: File '{filename}' is not allowed.")
    return
  if os.path.exists(filename):
    os.startfile(filename)
  else:
    print(f"Error: File '{filename}' not found.")

def main():
  """
  Prompts user for filename and calls view_document function.
  """
  filename = input("Enter filename (including extension): ")
  view_document(filename)

if __name__ == "__main__":
  main()