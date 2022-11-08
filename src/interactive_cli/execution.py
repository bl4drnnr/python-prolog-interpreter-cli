import curses

from src.common.exceptions import WrongJsonFormat, WrongFactFormat

from src.interactive_cli.prints import print_logo
from src.interactive_cli.docs import commands_docs

from src.common.functions import print_raw_input, print_text

from src.operations.json_converter import json_converter
from src.operations.compile_prolog import compile_and_execute_prolog_program
from src.operations.fetch_data import fetch_data


def command_execution(stdscr, command):
    stdscr.clear()
    print_logo(stdscr, 4)

    command_instructions = commands_docs[command]['short']

    for idx, row in enumerate(command_instructions):
        if idx == 0:
            stdscr.addstr(f' - {row}', curses.A_BOLD)
        else:
            stdscr.addstr(row)

    try:
        if command == 'Read from JSON':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

            json_converter('read', path_input_file, path_output_file, stdscr)
        elif command == 'Write to JSON':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

            json_converter('write', path_input_file, path_output_file, stdscr)
        elif command == 'Compile Prolog':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

            compile_and_execute_prolog_program(path_input_file, path_output_file, stdscr)
        elif command == 'Fetch data':
            url = print_raw_input(stdscr, 'Provide source of data you want to get: ').strip()

            fetch_data(url)
    except WrongFactFormat:
        print_text('Wrong fact format!', stdscr, error=True)
    except WrongJsonFormat:
        print_text('Wrong JSON file format!', stdscr, error=True)

    stdscr.addstr('\n\nPress any key to get back...\n\n')
    stdscr.addstr('#################################', curses.A_BOLD)
    stdscr.getch()
