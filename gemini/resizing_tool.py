import os
import sys
from PIL import Image

def resize_image(input_file, output_file, width, height):
    """Resizes an image to the specified dimensions.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to the output image file.
        width (int): The desired width of the resized image.
        height (int): The desired height of the resized image.
    """

    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input image file '{input_file}' not found.")

        # Open the image using Pillow
        with Image.open(input_file) as img:
            # Validate the input dimensions
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive integers.")

            # Resize the image
            resized_img = img.resize((width, height))

            # Save the resized image
            resized_img.save(output_file)

            print(f"Image resized successfully. Output saved to '{output_file}'.")

    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to handle user input and call the resize_image function."""

    while True:
        input_file = input("Enter the path to the input image file: ")
        output_file = input("Enter the path to the output image file: ")
        try:
            width = int(input("Enter the desired width: "))
            height = int(input("Enter the desired height: "))
        except ValueError:
            print("Invalid input. Width and height must be integers.")
            continue

        resize_image(input_file, output_file, width, height)

        if input("Do you want to resize another image? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()