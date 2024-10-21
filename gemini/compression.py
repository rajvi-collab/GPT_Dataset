import argparse
import os
import shutil
import subprocess

def compress_directory(directory, output_file):
    """Compresses a directory using 7zip.

    Args:
        directory: The directory to compress.
        output_file: The name of the compressed file.
    """

    command = ["7z", "a", output_file, directory]
    try:
        subprocess.run(command, check=True)
        print(f"Compressed {directory} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error compressing {directory}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Compress directories using 7zip.")
    parser.add_argument("directories", nargs="+", help="The directories to compress.")
    parser.add_argument("-o", "--output", default="compressed.7z", help="The output file name.")
    args = parser.parse_args()

    for directory in args.directories:
        if os.path.isdir(directory):
            compress_directory(directory, args.output)
        else:
            print(f"{directory} is not a directory.")

if __name__ == "__main__":
    main()