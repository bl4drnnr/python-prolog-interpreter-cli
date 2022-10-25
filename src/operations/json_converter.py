from src.common.files.read_file import read_file
from src.common.files.write_file import write_file

from src.common.checkers.check_json_format import check_json_format


def json_to_prolog(path_input_file, path_output_file, stdscr=None):
    output_program = ''

    read_data = read_file(path_input_file, stdscr)
    data = check_json_format(read_data)

    for predicate in data['predicates']:
        output_program += f"{predicate['name']}({', '.join(predicate['arguments'])}).\n"

    for fact in data['facts']:
        output_program += f"{fact['name']}({', '.join(fact['arguments'])}):-"
        for index, condition in enumerate(fact['conditions']):
            if condition['type'] == 'predicate':
                output_program += f"{condition['name']}({', '.join(condition['arguments'])})"
            if len(fact['joins']):
                output_program += fact['joins'][index]
        output_program += '.\n'

    write_file(output_program, path_output_file, stdscr)


def prolog_to_json(path_input_file, path_output_file, stdscr=None):
    output_program = ''
    read_data = read_file(path_input_file, stdscr)


def json_converter(operation_type, path_input_file, path_output_file, stdscr=None):
    if operation_type == 'read':
        json_to_prolog(path_input_file, path_output_file, stdscr)
    elif operation_type == 'write':
        prolog_to_json(path_input_file, path_output_file, stdscr)
