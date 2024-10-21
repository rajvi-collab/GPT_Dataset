import subprocess
import shlex

def execute_shell_command(user_input: str):
    """
    Executes a shell command based on user input in a safe manner to avoid shell injection.
    
    Parameters:
        user_input (str): The shell command input from the user.
        
    Returns:
        output (str): The standard output of the command.
        error (str): The standard error of the command, if any.
    """
    try:
        # Split the command into a safe list using shlex.split to avoid shell injection
        command = shlex.split(user_input)
        
        # Execute the command without using the shell
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Return the output and any error
        return result.stdout, result.stderr
    
    except subprocess.CalledProcessError as e:
        return e.output, e.stderr
    except Exception as e:
        return None, str(e)

# Example usage
user_command = input("Enter a shell command: ")
output, error = execute_shell_command(user_command)

if output:
    print("Command output:", output)
if error:
    print("Command error:", error)
