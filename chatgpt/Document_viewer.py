from flask import Flask, request, send_file, abort, render_template_string
from functools import wraps

app = Flask(__name__)

# Example users and their allowed files (in real implementation, this might be stored in a database)
USERS = {
    'user1': {'password': 'password123', 'allowed_files': ['file1.txt', 'file2.txt']},
    'user2': {'password': 'password456', 'allowed_files': ['file3.txt']}
}

# Basic HTML template to show the document content or access denied
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Document Viewer</title></head>
<body>
<h2>{{ message }}</h2>
{% if file_content %}
<pre>{{ file_content }}</pre>
{% endif %}
</body>
</html>
"""

# Authentication function to check credentials
def authenticate(username, password):
    user = USERS.get(username)
    if user and user['password'] == password:
        return user
    return None

# Decorator to require authentication and check access to the file
def requires_auth_and_access(filename):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or not authenticate(auth.username, auth.password):
                return abort(401, description="Authentication required")
            
            user = USERS[auth.username]
            if filename not in user['allowed_files']:
                return abort(403, description="Access denied")

            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/view/<filename>', methods=['GET'])
@requires_auth_and_access(filename='<filename>')
def view_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return render_template_string(HTML_TEMPLATE, message=f"Viewing: {filename}", file_content=content)
    except FileNotFoundError:
        return abort(404, description="File not found")
    except Exception as e:
        return abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
