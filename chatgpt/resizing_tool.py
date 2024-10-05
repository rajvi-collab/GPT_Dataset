from PIL import Image
import os

def validate_image_file(file_path):
    """Check if the file exists and is a valid image format."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        img = Image.open(file_path)
        img.verify()  # Verify that it is indeed an image file
    except (IOError, SyntaxError) as e:
        raise ValueError(f"Invalid image file: {file_path}") from e

def validate_dimensions(width, height):
    """Check if the provided dimensions are positive integers."""
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")

def resize_image(input_path, output_path, width, height, keep_aspect_ratio=True):
    """
    Resize the image to the specified width and height.
    - If keep_aspect_ratio is True, the aspect ratio will be maintained.
    """
    # Validate the input image file
    validate_image_file(input_path)
    
    # Validate the dimensions
    validate_dimensions(width, height)

    try:
        # Open the image
        with Image.open(input_path) as img:
            # Preserve aspect ratio if required
            if keep_aspect_ratio:
                img.thumbnail((width, height), Image.ANTIALIAS)
            else:
                img = img.resize((width, height), Image.ANTIALIAS)
            
            # Save the resized image
            img.save(output_path)
            print(f"Image successfully resized and saved to {output_path}.")
    except Exception as e:
        print(f"Error resizing the image: {str(e)}")
        raise

def main():
    # Example usage:
    input_image_path = 'path_to_input_image.jpg'
    output_image_path = 'path_to_output_image.jpg'
    
    # Desired dimensions
    new_width = 800
    new_height = 600
    
    try:
        resize_image(input_image_path, output_image_path, new_width, new_height, keep_aspect_ratio=True)
    except Exception as e:
        print(f"Failed to resize image: {e}")

# Commented out function calls to prevent execution
# main()
