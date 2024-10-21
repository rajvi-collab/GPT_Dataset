import os

def load_template(template_name):
  """Loads a template from the templates directory.

  Args:
    template_name: The name of the template file (e.g., "index.html").

  Returns:
    The contents of the template file as a string, or None if the file is not found.
  """
  templates_dir = os.path.join(os.path.dirname(__file__), "templates")  # Safe path
  template_path = os.path.join(templates_dir, template_name)

  if not os.path.isfile(template_path):
    return None

  with open(template_path, 'r') as f:
    return f.read()

# Example usage
template_content = load_template("welcome.html")
if template_content:
  print(template_content)
else:
  print("Template not found.")