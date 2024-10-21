import configparser
import os
import re

def update_config_file(config_file_path, section, key, value):
    """
    Updates a configuration file with user input.

    Args:
        config_file_path (str): Path to the configuration file.
        section (str): Section name in the configuration file.
        key (str): Key name in the section.
        value (str): New value for the key.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    # Validate input
    if not re.match(r'^[a-zA-Z0-9_]+$', section):
        raise ValueError("Invalid section name")
    if not re.match(r'^[a-zA-Z0-9_]+$', key):
        raise ValueError("Invalid key name")
    if not isinstance(value, str):
        raise ValueError("Value must be a string")

    # Create a configparser object
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Update the configuration
    if section not in config:
        config[section] = {}
    config[section][key] = value

    # Write the updated configuration to the file
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)

    return True


def main():
    config_file_path = input("Enter the configuration file path: ")
    section = input("Enter the section name: ")
    key = input("Enter the key name: ")
    value = input("Enter the new value: ")

    try:
        if update_config_file(config_file_path, section, key, value):
            print("Configuration file updated successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()