import curses

from src.common.exceptions import WrongJsonFormat

from src.interactive_cli.prints import print_logo
from src.interactive_cli.docs import commands_docs

from src.common.functions import print_raw_input, print_text

from src.operations.json_converter import json_converter
from src.operations.compile_prolog import compile_and_execute_prolog_program


def command_execution(stdscr, command):
    stdscr.clear()
    print_logo(stdscr, 4)

    command_instructions = commands_docs[command]['short']

    for idx, row in enumerate(command_instructions):
        if idx == 0:
            stdscr.addstr(f' - {row}', curses.A_BOLD)
        else:
            stdscr.addstr(row)

    path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
    path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

    try:
        if command == 'Read from JSON':
            json_converter('read', path_input_file, path_output_file, stdscr)
        elif command == 'Write to JSON':
            json_converter('write', path_input_file, path_output_file, stdscr)
        elif command == 'Compile Prolog':
            compile_and_execute_prolog_program(path_input_file, path_output_file, stdscr)
    except WrongJsonFormat:
        print_text('Wrong JSON file format!', stdscr, error=True)

    stdscr.addstr('\n\nPress any key to get back...\n\n')
    stdscr.addstr('#################################', curses.A_BOLD)
    stdscr.getch()
