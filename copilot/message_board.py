import http.server
import socketserver
import urllib.parse

PORT = 8000
messages = []

class MessageBoardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.generate_html().encode())
        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode())
        username = params.get('username', [''])[0]
        message = params.get('message', [''])[0]
        if username and message:
            messages.append({'user': username, 'message': message})
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def generate_html(self):
        html = '<html><body>'
        html += '<h1>Message Board</h1>'
        html += '<form method="post">'
        html += 'Username: <input type="text" name="username"><br>'
        html += 'Message: <textarea name="message"></textarea><br>'
        html += '<input type="submit" value="Post">'
        html += '</form>'
        html += '<h2>Messages</h2>'
        html += '<ul>'
        for message in messages:
            html += f'<li><strong>{message["user"]}:</strong> {message["message"]}</li>'
        html += '</ul>'
        html += '</body></html>'
        return html

with socketserver.TCPServer(("", PORT), MessageBoardHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
