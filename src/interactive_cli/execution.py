import curses

from src.common.exceptions import WrongJsonFormat, WrongFactFormat

from src.interactive_cli.prints import print_logo
from src.interactive_cli.docs import commands_docs

from src.common.functions import print_raw_input, print_text

from src.operations.json_toolbox import JsonParser, JsonFormatChecker
from src.operations.prolog_toolbox import PrologParser, PrologFormatChecker


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

        elif command == 'Write to JSON':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

        elif command == 'Compile Prolog':
            path_input_file = print_raw_input(stdscr, 'Please, provide path to input file: ').strip()
            path_output_file = print_raw_input(stdscr, 'Please, provide path for output file: ').strip()

        elif command == 'Fetch data':
            url = print_raw_input(stdscr, 'Provide source of data you want to get: ').strip()

    except WrongFactFormat:
        print_text('Wrong fact format!', stdscr, error=True)
    except WrongJsonFormat:
        print_text('Wrong JSON file format!', stdscr, error=True)

    stdscr.addstr('\n\nPress any key to get back...\n\n')
    stdscr.addstr('#################################', curses.A_BOLD)
    stdscr.getch()
