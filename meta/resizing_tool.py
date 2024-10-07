from PIL import Image
import os

def resize_image(image_path, output_path, new_width, new_height):
    """
    Resizes an image to specified dimensions.

    Args:
    image_path (str): Path to the input image file.
    output_path (str): Path to save the resized image file.
    new_width (int): Desired width of the resized image.
    new_height (int): Desired height of the resized image.

    Raises:
    ValueError: If the image file is invalid or dimensions are non-positive.
    OSError: If the image file cannot be opened or saved.
    """

    # Validate input dimensions
    if new_width <= 0 or new_height <= 0:
        raise ValueError("Dimensions must be positive integers.")

    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Validate image file
            if img.format not in ['JPEG', 'PNG', 'BMP', 'TIFF']:
                raise ValueError("Unsupported image format.")

            # Resize the image
            img = img.resize((new_width, new_height))

            # Save the resized image
            img.save(output_path)

    except OSError as e:
        raise OSError(f"Error processing image: {e}")


def main():
    # Get user input
    image_path = input("Enter the image file path: ")
    output_path = input("Enter the output file path: ")
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))

    # Validate file paths
    if not os.path.isfile(image_path):
        print("Error: Input file does not exist.")
        return

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Resize the image
        resize_image(image_path, output_path, new_width, new_height)
        print("Image resized successfully.")

    except (ValueError, OSError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()