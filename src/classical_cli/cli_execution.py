import sys

from src.classical_cli.exceptions import WrongOption

from src.operations.json_converter import json_converter
from src.operations.compile_prolog import compile_and_execute_prolog_program


def cli_execution(operation, options):
    path_to_file = options['file']

    try:
        if operation == 'read':
            json_converter('read')
        elif operation == 'write':
            json_converter('write')
        elif operation == 'compile':
            compile_and_execute_prolog_program()
        else:
            raise WrongOption
    except WrongOption:
        print('Wrong option!')
        sys.exit()
