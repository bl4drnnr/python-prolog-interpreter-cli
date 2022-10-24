from src.common.functions import print_text


def write_file(stdscr=None):
    try:
        pass
    except Exception as e:
        error = f'An error occurred while while writing file: {e}'
        print_text(error, stdscr, error=True)
