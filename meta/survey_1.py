import http.server
import socketserver
import os
import urllib.parse

# Survey data stored in memory for simplicity
surveys = {}

class SurveyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_parts = urllib.parse.urlparse(self.path)
        path = url_parts.path
 
        if path == '/create':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <body>
                <h1>Create Survey</h1>
                <form action="/create" method="post">
                <input type="text" name="title" placeholder="Survey Title"><br>
                <input type="text" name="question" placeholder="Survey Question"><br>
                <input type="text" name="options" placeholder="Options (comma separated)"><br>
                <input type="submit" value="Create">
                </form>
                </body>
                </html>
            """)
        elif path.startswith('/survey/'):
            survey_id = path.split('/')[-1]
            if survey_id in surveys:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                survey = surveys[survey_id]
                self.wfile.write(f"""
                    <html>
                    <body>
                    <h1>{survey['title']}</h1>
                    <p>{survey['question']}</p>
                    <form action="/survey/{survey_id}" method="post">
                    {"".join(f"<input type='radio' name='answer' value='{option}'>{option}<br>" for option in survey['options'].split(','))}
                    <input type="submit" value="Vote">
                    </form>
                    </body>
                    </html>
                """.encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Survey not found")
        elif path == '/export':
            survey_id = urllib.parse.parse_qs(url_parts.query)['survey_id'][0]
            if survey_id in surveys:
                self.send_response(200)
                self.send_header('Content-type', 'text/csv')
                self.send_header('Content-Disposition', f'attachment; filename={survey_id}.csv')
                self.end_headers()
                survey = surveys[survey_id]
                self.wfile.write(f"Title,{survey['title']}\nQuestion,{survey['question']}\nOptions,{survey['options']}\n".encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Survey not found")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Not found")

    def do_POST(self):
        url_parts = urllib.parse.urlparse(self.path)
        path = url_parts.path
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        if path == '/create':
            survey_data = urllib.parse.parse_qs(body.decode())
            survey_id = str(len(surveys))
            surveys[survey_id] = {
                'title': survey_data['title'][0],
                'question': survey_data['question'][0],
                'options': survey_data['options'][0]
            }
            self.send_response(302)
            self.send_header('Location', f'/survey/{survey_id}')
            self.end_headers()
        elif path.startswith('/survey/'):
            survey_id = path.split('/')[-1]
            if survey_id in surveys:
                survey_data = urllib.parse.parse_qs(body.decode())
                answer = survey_data['answer'][0]
                # Store answer in survey data
                surveys[survey_id]['answers'] = surveys[survey_id].get('answers', [])
                surveys[survey_id]['answers'].append(answer)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Vote recorded")
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Survey not found")

def run_server():
    port = 8000
    with socketserver.TCPServer(("", port), SurveyHandler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
    
    