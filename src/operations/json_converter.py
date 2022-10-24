from src.common.read_file import read_file

from src.common.variables import JSON_FORMAT


def json_to_prolog(file_path, stdscr=None):
    data = read_file(file_path, stdscr)

    for key, value in data.items():
        pass


def prolog_to_json(file_path, stdscr=None):
    read_file(file_path, stdscr)


def json_converter(operation_type, file_path, stdscr=None):
    if operation_type == 'read':
        json_to_prolog(file_path, stdscr)
    elif operation_type == 'write':
        prolog_to_json(file_path, stdscr)
