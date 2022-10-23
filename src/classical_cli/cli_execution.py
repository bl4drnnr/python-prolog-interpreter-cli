import sys

from src.classical_cli.exceptions import WrongOption

from src.operations.json_converter import json_converter
from src.operations.compile_prolog import compile_and_execute_prolog_program


def cli_execution(operation, options):
    path_to_file = options['file']

    try:
        if operation == 'read':
            json_converter('read', path_to_file)
        elif operation == 'write':
            json_converter('write', path_to_file)
        elif operation == 'compile':
            compile_and_execute_prolog_program(path_to_file)
        else:
            raise WrongOption
    except WrongOption:
        print('Wrong option!')
        sys.exit()
