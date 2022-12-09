import os
from src.common.functions import print_text


def write_file(data, output_file, stdscr=None):
    try:
        if isinstance(data, str):
            data = data.encode('utf-8')
        with open(os.path.expanduser(output_file), 'w') as f:
            f.write(str(data).replace("'", '"'))
        f.close()
        return True
    except Exception as e:
        error = f'An error occurred while while writing file: {e}'
        print_text(error, stdscr, error=True)
