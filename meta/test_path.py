import requests

def test_path_traversal():
    base_url = 'http://localhost:8000'

    # Test valid file download
    response = requests.get(f'{base_url}/file.txt')
    assert response.status_code == 200

    # Test path traversal attempts
    traversal_attempts = [
        '../secret.txt',
        '/etc/passwd',
        '../../etc/passwd',
        '%2e%2e%2fetc%2fpasswd',  # URL-encoded traversal
    ]

    for attempt in traversal_attempts:
        response = requests.get(f'{base_url}/{attempt}')
        assert response.status_code == 404, f'Traversal attempt succeeded: {attempt}'

if __name__ == '__main__':
    test_path_traversal()