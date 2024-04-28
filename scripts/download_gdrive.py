'''
Guide for usage:
In your terminal, run the command:

python download_gdrive.py GoogleFileID /path/for/this/file/to/download/file.type

'''

import requests
import gdown
from tqdm import tqdm

def download_file_from_google_drive(file_id, destination):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, destination, quiet=False)


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)
