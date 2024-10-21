import subprocess
import shlex

def execute_code(code, language):
    """Executes the given code snippet in the specified language.

    Args:
        code (str): The code snippet to execute.
        language (str): The programming language of the code.

    Raises:
        ValueError: If the language is not supported.
        subprocess.CalledProcessError: If the code execution fails.
    """

    supported_languages = {
        "python": "python",
        "javascript": "node",
        # Add more languages as needed
    }

    if language not in supported_languages:
        raise ValueError(f"Unsupported language: {language}")

    interpreter = supported_languages[language]

    # Use shlex.quote to safely escape command arguments
    command = f"{interpreter} -c '{shlex.quote(code)}'"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise e

# Test for OS Command Injection
malicious_code = "; rm -rf /"  # Replace with your desired malicious code
try:
    output = execute_code(malicious_code, "python")  # Or any supported language
    print(output)
except subprocess.CalledProcessError as e:
    print(f"OS Command Injection prevented: {e}")
    
