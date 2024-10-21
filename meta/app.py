from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Supported languages
LANGUAGES = ['python', 'java', 'c++']

@app.route('/run', methods=['POST'])
def run_code():
    language = request.json['language']
    code = request.json['code']

    if language not in LANGUAGES:
        return jsonify({'error': 'Unsupported language'}), 400

    # Create a new container for code execution
    container_name = f'code-exec-{language}'
    subprocess.run(f'docker-compose up -d {container_name}', shell=True)

    # Copy code to container
    subprocess.run(f'docker cp {code} {container_name}:/app/', shell=True)

    # Execute code in container
    output = subprocess.run(f'docker exec {container_name} {language} /app/{code}', shell=True, capture_output=True)

    # Remove container
    subprocess.run(f'docker-compose down {container_name}', shell=True)

    return jsonify({'output': output.stdout.decode()}), 200

if __name__ == '__main__':
    app.run(debug=True)