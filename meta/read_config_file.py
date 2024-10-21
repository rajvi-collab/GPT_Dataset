import configparser
import os
import tempfile
from cryptography.fernet import Fernet


def read_config_file(file_path, encrypted=False, key=None):
    """
    Reads a configuration file securely.

    Args:
        file_path (str): Path to the configuration file.
        encrypted (bool, optional): Whether the config file is encrypted. Defaults to False.
        key (str, optional): Encryption key (required if encrypted=True). Defaults to None.

    Returns:
        dict: Configuration data.
    """
    config = configparser.ConfigParser()

    if encrypted:
        # Decrypt the config file using Fernet
        if key is None:
            raise ValueError("Encryption key required")
        f = Fernet(key)
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        config.read_string(decrypted_data.decode('utf-8'))
    else:
        # Read the config file directly
        config.read(file_path)

    # Convert config sections to a dictionary
    config_dict = {section: dict(config.items(section)) for section in config.sections()}

    return config_dict


def write_config_file(file_path, config_data, encrypted=False, key=None):
    """
    Writes a configuration file securely.

    Args:
        file_path (str): Path to the configuration file.
        config_data (dict): Configuration data.
        encrypted (bool, optional): Whether to encrypt the config file. Defaults to False.
        key (str, optional): Encryption key (required if encrypted=True). Defaults to None.
    """
    config = configparser.ConfigParser()

    # Convert dictionary to config sections
    for section, data in config_data.items():
        config[section] = data

    if encrypted:
        # Write config to temporary file
        with tempfile.TemporaryFile(mode='w+t') as tmp_file:
            config.write(tmp_file)
            tmp_file.seek(0)
            # Encrypt the config data using Fernet
            if key is None:
                raise ValueError("Encryption key required")
            f = Fernet(key)
            with open(file_path, 'wb') as file:
                file.write(f.encrypt(tmp_file.read().encode('utf-8')))
    else:
        # Write the config file directly
        with open(file_path, 'w') as file:
            config.write(file)


# Example usage
if __name__ == "__main__":
    # Generate encryption key
    encryption_key = Fernet.generate_key()

    # Define config data
    config_data = {
        'section1': {'key1': 'value1', 'key2': 'value2'},
        'section2': {'key3': 'value3', 'key4': 'value4'}
    }

    # Write encrypted config file
    config_file_path = 'encrypted_config.ini'
    write_config_file(config_file_path, config_data, encrypted=True, key=encryption_key)

    # Read encrypted config file
    read_config = read_config_file(config_file_path, encrypted=True, key=encryption_key)

    print("Encryption Key:", encryption_key)
    print("Config Data:", config_data)
    print("Read Config:", read_config)