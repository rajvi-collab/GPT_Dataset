import os
import configparser
import pathlib
from cryptography.fernet import Fernet


# Securely read a configurati   on file
def read_config(config_path: str):
    # Validate if the file exists
    config_file = pathlib.Path(config_path)
    if not config_file.exists() or not config_file.is_file():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    # Load configparser
    config = configparser.ConfigParser()

    # Read the config file
    config.read(config_path)

    return config

# Decrypt sensitive data (if stored encrypted)
def decrypt_value(encrypted_value: str, key: str):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_value.encode()).decode()

# Fetch a sensitive environment variable
def get_env_variable(key: str):
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Missing required environment variable: {key}")
    return value

def main():
    config_path = 'config.ini'
    
    # Read the configuration file
    try:
        config = read_config(config_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    # Fetch sensitive data (like DB password) securely from environment variables
    try:
        db_password = get_env_variable("DB_PASSWORD")
    except ValueError as e:
        print(e)
        return

    # Access configuration values
    db_host = config.get('database', 'host', fallback='localhost')
    db_port = config.getint('database', 'port', fallback=5432)
    db_user = config.get('database', 'user', fallback='root')

    # Display the database configuration
    print(f"Database Configuration: Host={db_host}, Port={db_port}, User={db_user}, Password={db_password}")

if __name__ == "__main__":
    main()
