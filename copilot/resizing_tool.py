from PIL import Image
import os

def is_valid_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False

def resize_image(input_path, output_path, width, height):
    if not os.path.isfile(input_path):
        raise ValueError("The input file does not exist.")
    
    if not is_valid_image(input_path):
        raise ValueError("The input file is not a valid image.")
    
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height), Image.ANTIALIAS)
            resized_img.save(output_path)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path to save the resized image: ")
    try:
        width = int(input("Enter the width for the resized image: "))
        height = int(input("Enter the height for the resized image: "))
    except ValueError:
        print("Width and height must be integers.")
        return
    
    try:
        resize_image(input_path, output_path, width, height)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
