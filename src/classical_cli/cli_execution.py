import sys

from src.common.exceptions import WrongOption, WrongJsonFormat

from src.operations.json_converter import json_converter
from src.operations.compile_prolog import compile_and_execute_prolog_program


def cli_execution(operation, options):
    path_input_file = options['input_file']
    path_output_file = options['output_file']

    try:
        if operation == 'read':
            json_converter('read', path_input_file, path_output_file)
        elif operation == 'write':
            json_converter('write', path_input_file, path_output_file)
        elif operation == 'compile':
            compile_and_execute_prolog_program(path_input_file, path_output_file)
        else:
            raise WrongOption
    except WrongOption:
        print('Wrong option!')
        sys.exit()
    except WrongJsonFormat:
        print('Wrong JSON file format!')
        sys.exit()
