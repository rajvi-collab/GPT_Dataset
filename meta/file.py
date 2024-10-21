import http.server
import os
import urllib.parse

# Intended directory for file downloads
DOWNLOAD_DIR = 'file_download'

class FileDownloadRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse URL path
        parsed_path = urllib.parse.urlparse(self.path)
        file_path = parsed_path.path.strip('/')

        # Check if file exists in download directory
        if os.path.exists(os.path.join(DOWNLOAD_DIR, file_path)):
            self.send_response(200)
            self.send_header('Content-Disposition', f'attachment; filename="{file_path}"')
            self.end_headers()
            with open(os.path.join(DOWNLOAD_DIR, file_path), 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'File not found')

def run_server():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, FileDownloadRequestHandler)
    print('File download service running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    
    