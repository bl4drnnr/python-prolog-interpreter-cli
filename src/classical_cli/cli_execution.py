import sys

from src.common.exceptions import WrongOption, WrongJsonFormat, WrongFactFormat

from src.operations.json_toolbox.JsonParser import JsonParser
from src.operations.json_toolbox.JsonFormatChecker import JsonFormatChecker
from src.operations.prolog_toolbox.PrologParser import PrologParser
from src.operations.prolog_toolbox.PrologFormatChecker import PrologFormatChecker


def check_for_options(options, required_options):
    for option in options:
        if option not in required_options:
            raise WrongOption


def cli_execution(operation, options):
    try:
        if operation == 'read':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            json_converter('read', options['input_file'], options['output_file'])
        elif operation == 'write':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            json_converter('write', options['input_file'], options['output_file'])
        elif operation == 'compile':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            compile_and_execute_prolog_program(options['input_file'], options['output_file'])
        elif operation == 'fetch':
            required_options = ['url']
            check_for_options(options, required_options)

            fetch_data(options['url'])
        else:
            raise WrongOption
    except WrongOption:
        print('Wrong option!')
        sys.exit()
    except WrongFactFormat:
        print('Wrong fact format!')
        sys.exit()
    except WrongJsonFormat:
        print('Wrong JSON file format!')
        sys.exit()
