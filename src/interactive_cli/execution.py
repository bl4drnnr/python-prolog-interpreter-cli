import curses

from src.interactive_cli.prints import print_logo
from src.interactive_cli.docs import commands_docs

from src.common.functions import print_raw_input

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

    path_to_file = print_raw_input(stdscr, 'Please, provide path to file: ').strip()

    if command == 'Read from JSON':
        json_converter('read', path_to_file)
    elif command == 'Write to JSON':
        json_converter('write', path_to_file)
    elif command == 'Compile Prolog':
        compile_and_execute_prolog_program(path_to_file)
    else:
        return
