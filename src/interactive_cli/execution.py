import curses

from src.common.exceptions import WrongJsonFormat, WrongFactFormat

from src.interactive_cli.prints import print_logo
from src.interactive_cli.docs import commands_docs

from src.common.functions import print_raw_input, print_text

from src.operations.json_toolbox.JsonParser import JsonParser
from src.operations.json_toolbox.JsonFormatChecker import JsonFormatChecker
from src.operations.prolog_toolbox.PrologParser import PrologParser
from src.operations.prolog_toolbox.PrologFormatChecker import PrologFormatChecker
from src.operations.compile.Compiler import Compiler
from src.operations.fetch.Fetch import Fetch

from src.common.files.read_file import read_file
from src.common.files.write_file import write_file


def command_execution(stdscr, command):
    stdscr.clear()
    print_logo(stdscr, 4)

    command_instructions = commands_docs[command]['short']

    for idx, row in enumerate(command_instructions):
        stdscr.addstr(f' - {row}', curses.A_BOLD) if idx == 0 else stdscr.addstr(row)

    try:
        if command == 'Read from JSON':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

            json_format_checker = JsonFormatChecker()
            json_parser = JsonParser()

            file_data = read_file(path_input_file)

            json_data = json_format_checker.check_json_format(file_data)
            output_program = json_parser.parse_json(json_data)

            write_file(output_program, path_output_file)
        elif command == 'Write to JSON':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

            prolog_format_checker = PrologFormatChecker()
            prolog_parser = PrologParser()

            file_data = read_file(path_input_file)

            prolog_data = prolog_format_checker.check_prolog_format(file_data)
            output_program = prolog_parser.parse_prolog(prolog_data)

            write_file({'data': output_program}, path_output_file)
        elif command == 'Compile Prolog':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()
            queries = print_raw_input(stdscr, 'Please, provide queries to execute: ').strip()

            file_data = read_file(path_input_file)
            json_format_checker = JsonFormatChecker()
            json_parser = JsonParser()

            compiler = Compiler(json_parser, json_format_checker)
            execution_result = compiler.execute_code(file_data, queries)

            write_file(execution_result, path_output_file)

        elif command == 'Fetch data':
            url = print_raw_input(stdscr, 'Provide source of data you want to get: ').strip()

            fetcher = Fetch()
            data = fetcher.fetch_data(url)
    except WrongFactFormat:
        print_text('Wrong fact format!', stdscr, error=True)
    except WrongJsonFormat:
        print_text('Wrong JSON file format!', stdscr, error=True)

    stdscr.addstr('\n\nPress any key to get back...\n\n')
    stdscr.addstr('#################################', curses.A_BOLD)
    stdscr.getch()
