import sys

from src.common.exceptions import WrongOption, WrongJsonFormat, WrongFactFormat

from src.operations.json_toolbox.JsonParser import JsonParser
from src.operations.json_toolbox.JsonFormatChecker import JsonFormatChecker
from src.operations.prolog_toolbox.PrologParser import PrologParser
from src.operations.prolog_toolbox.PrologFormatChecker import PrologFormatChecker
from src.operations.compile.Compiler import Compiler
from src.operations.fetch.Fetch import Fetch

from src.common.files.read_file import read_file
from src.common.files.write_file import write_file


def check_for_options(options, required_options):
    for option in options:
        if option not in required_options:
            raise WrongOption


def cli_execution(operation, options):
    try:
        if operation == 'read':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            json_format_checker = JsonFormatChecker()
            json_parser = JsonParser()

            file_data = read_file(options['input_file'])

            json_data = json_format_checker.check_json_format(file_data)
            output_program = json_parser.parse_json(json_data)

            write_file(output_program, options['output_file'])
        elif operation == 'write':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            prolog_format_checker = PrologFormatChecker()
            prolog_parser = PrologParser()
            
            file_data = read_file(options['input_file'])

            prolog_data = prolog_format_checker.check_prolog_format(file_data)
            output_program = prolog_parser.parse_prolog(prolog_data)

            write_file({'data': output_program}, options['output_file'])
        elif operation == 'compile':
            required_options = ['input_file', 'output_file']
            check_for_options(options, required_options)

            file_data = read_file(options['input_file'])
            json_format_checker = JsonFormatChecker()
            json_parser = JsonParser()

            compiler = Compiler(json_parser, json_format_checker)
            execution_result = compiler.execute_code(file_data)

            write_file(execution_result, options['output_file'])
        elif operation == 'fetch':
            required_options = ['url']
            check_for_options(options, required_options)

            fetcher = Fetch()
            # data = fetcher.fetch_data()
        else:
            raise WrongOption
    except WrongOption as wo:
        print(wo.message)
        sys.exit()
    except WrongFactFormat as wff:
        print(wff.message)
        sys.exit()
    except WrongJsonFormat as wjf:
        print(wjf.message)
        sys.exit()
