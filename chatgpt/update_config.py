import configparser
import os

def load_config(file_path):
    """Load the configuration file."""
    config = configparser.ConfigParser()
    if os.path.exists(file_path):
        config.read(file_path)
    else:
        print(f"Configuration file '{file_path}' not found.")
    return config

def save_config(config, file_path):
    """Save the configuration file."""
    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"Configuration file '{file_path}' updated successfully.")

def get_valid_sections(config):
    """Get a list of valid sections in the config."""
    return config.sections()

def get_valid_options(config, section):
    """Get a list of valid options for a given section."""
    return config.options(section)

def update_configuration(file_path):
    """Main function to update configuration."""
    config = load_config(file_path)

    if not config:
        return

    print("Available sections:")
    sections = get_valid_sections(config)
    for section in sections:
        print(f"- {section}")

    section_to_update = input("Enter the section you want to update: ")
    if section_to_update not in sections:
        print("Invalid section. Exiting.")
        return

    print(f"Available options in '{section_to_update}':")
    options = get_valid_options(config, section_to_update)
    for option in options:
        print(f"- {option}")

    option_to_update = input("Enter the option you want to update: ")
    if option_to_update not in options:
        print("Invalid option. Exiting.")
        return

    new_value = input(f"Enter the new value for '{option_to_update}': ")

    # Update the configuration
    config.set(section_to_update, option_to_update, new_value)

    # Save the updated configuration
    save_config(config, file_path)

if __name__ == "__main__":
    config_file = "config.ini"  # Path to the configuration file
    update_configuration(config_file)
