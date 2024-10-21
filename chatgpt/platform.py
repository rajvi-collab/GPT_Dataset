import subprocess
import shlex

def execute_code(language, code):
    try:
        # Define command based on the language
        if language == 'python':
            cmd = f"python3 -c {shlex.quote(code)}"
        elif language == 'bash':
            cmd = f"bash -c {shlex.quote(code)}"
        else:
            return "Unsupported language"

        # Execute the command securely using subprocess
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=10)

        return result.stdout if result.returncode == 0 else result.stderr
    except subprocess.TimeoutExpired:
        return "Execution timed out"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
print(execute_code('python', 'print("Hello World")'))
