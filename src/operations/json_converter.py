from src.common.read_file import read_file
from src.common.write_file import write_file

from src.common.json_format_rules import JSON_FORMAT, ALLOWED_CONDITIONS_TYPES
from src.common.exceptions import WrongJsonFormat, WrongFactFormat


def check_file_format(data):
    predicates = []
    facts = []

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

        elif key == 'fact':

            if len(value['conditions']) == 0:
                raise WrongFactFormat

            if 'arguments' not in value or type(value['arguments']).__name__ != 'list':
                raise WrongFactFormat

            if \
                    "joins" not in value or \
                    type(value['joins']).__name__ != 'list' or \
                    len(value['joins']) != len(value['conditions']) - 1:
                raise WrongFactFormat

            for condition in value['conditions']:
                if 'type' not in condition:
                    raise WrongFactFormat
                if condition['type'] not in ALLOWED_CONDITIONS_TYPES:
                    raise WrongFactFormat
                if condition['type'] == 'predicate':
                    if 'arguments' not in condition or type(condition['arguments']).__name__ != 'list':
                        raise WrongFactFormat

            facts.append(value)

    return {
        'predicates': predicates,
        'facts': facts
    }


def json_to_prolog(path_input_file, path_output_file, stdscr=None):
    output_program = ''

    read_data = read_file(path_input_file, stdscr)
    data = check_file_format(read_data)

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
    read_file(path_input_file, stdscr)


def json_converter(operation_type, path_input_file, path_output_file, stdscr=None):
    if operation_type == 'read':
        json_to_prolog(path_input_file, path_output_file, stdscr)
    elif operation_type == 'write':
        prolog_to_json(path_input_file, path_output_file, stdscr)
