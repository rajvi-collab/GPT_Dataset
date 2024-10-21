import os
import tarfile
import zipfile
import argparse

def compress_directory(directory, output_file, compression_type='zip'):
    """
    Compress a directory.

    Args:
        directory (str): Path to the directory to compress.
        output_file (str): Path to the output compressed file.
        compression_type (str, optional): Type of compression. Defaults to 'zip'.
            Options: 'zip', 'tar', 'tar.gz', 'tar.bz2'
    """
    if compression_type not in ['zip', 'tar', 'tar.gz', 'tar.bz2']:
        raise ValueError("Invalid compression type")

    if compression_type == 'zip':
        with zipfile.ZipFile(output_file, 'w') as zip_file:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, directory))
    elif compression_type in ['tar', 'tar.gz', 'tar.bz2']:
        mode = 'w'
        if compression_type == 'tar.gz':
            mode += ':gz'
        elif compression_type == 'tar.bz2':
            mode += ':bz2'
        with tarfile.open(output_file, mode) as tar_file:
            tar_file.add(directory)

def main():
    parser = argparse.ArgumentParser(description='Compress directories')
    parser.add_argument('directory', help='Path to the directory to compress')
    parser.add_argument('-o', '--output', required=True, help='Path to the output compressed file')
    parser.add_argument('-c', '--compression', choices=['zip', 'tar', 'tar.gz', 'tar.bz2'], default='zip',
                        help='Type of compression')
    args = parser.parse_args()

    compress_directory(args.directory, args.output, args.compression)

if __name__ == '__main__':
    main()