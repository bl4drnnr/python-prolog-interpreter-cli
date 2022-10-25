import os
import json

from src.common.functions import print_text


def read_file(file_path, stdscr=None):
    try:
        with open(os.path.expanduser(file_path), mode='r') as f:
            data = f.read()
            return json.loads(data)
    except Exception as e:
        error = f'An error occurred while reading file: {e}'
        print_text(error, stdscr, error=True)

