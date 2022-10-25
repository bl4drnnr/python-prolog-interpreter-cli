from src.common.read_file import read_file
from src.common.write_file import write_file

from src.common.variables import JSON_FORMAT
from src.common.exceptions import WrongJsonFormat


def json_to_prolog(path_input_file, path_output_file, stdscr=None):
    predicates = []

    output_program = ''

    data = read_file(path_input_file, stdscr)

    for key, value in data.items():
        if key not in JSON_FORMAT:
            raise WrongJsonFormat
        else:
            for item_key, item_value in value.items():
                if item_key not in JSON_FORMAT[key]:
                    raise WrongJsonFormat
                if type(item_value).__name__ != JSON_FORMAT[key][item_key]:
                    raise WrongJsonFormat
        if key == 'predicate':
            predicates.append(value)

    for predicate in predicates:
        output_program += (predicate['name'] + '(' + ', '.join(predicate['arguments']) + ').\n')

    write_file(output_program, path_output_file, stdscr)


def prolog_to_json(path_input_file, path_output_file, stdscr=None):
    read_file(path_input_file, stdscr)


def json_converter(operation_type, path_input_file, path_output_file, stdscr=None):
    if operation_type == 'read':
        json_to_prolog(path_input_file, path_output_file, stdscr)
    elif operation_type == 'write':
        prolog_to_json(path_input_file, path_output_file, stdscr)
