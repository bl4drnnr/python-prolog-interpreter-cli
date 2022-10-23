import curses
import sys

from src.common.variables import MENU, LOGO, AVAILABLE_FUNCTIONS, PAD_HEIGHT
from src.common.functions import pad_refresh, navigation_control

from src.interactive_cli.docs import commands_docs


def print_logo(stdscr, color_pair_id):
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(LOGO):
        x = w // 2 - len(row) // 2
        stdscr.addstr(idx, x, row, curses.color_pair(color_pair_id))


def print_exit(stdscr):
    print_logo(stdscr, 4)
    stdscr.addstr('Hope, you had fun. See ya again...\n\n', curses.A_BOLD)

    stdscr.addstr('In case of any question, feel free to text me - ')
    stdscr.addstr('mikhail.bahdashych@protonmail.com\n\n', curses.A_BOLD | curses.A_UNDERLINE)

    stdscr.addstr('Press any key to exit...')
    stdscr.getch()
    sys.exit()


def print_documentation(stdscr):
    height, width = stdscr.getmaxyx()
    pad_pos = 0
    pad = curses.newpad(PAD_HEIGHT, width)

    print_logo(pad, 2)
    for doc_name, doc in commands_docs.items():
        pass

    pad_refresh(pad, pad_pos, height, width)
    navigation_control(pad, pad_pos, height, width)


def print_introduction(stdscr):
    print_logo(stdscr, 2)

    stdscr.addstr('PPIL (stands for Python Prolog Interpreter Library)', curses.A_BOLD)
    stdscr.addstr(' - is the program, that allows to use syntax of Prolog (logical programming language) ')
    stdscr.addstr('within Python programs.\n\n')

    stdscr.addstr('Right now, you are working with its CLI version. This CLI tool allows to ')
    stdscr.addstr('manage, convert (using JSON format), compile and execute Prolog programs.\n\n')

    stdscr.addstr('Use ')
    stdscr.addstr('ARROWS', curses.A_BOLD)
    stdscr.addstr(' on your keyboard for navigations.\n')
    stdscr.addstr('Press ')
    stdscr.addstr('ENTER', curses.A_BOLD)
    stdscr.addstr(' to confirm your choice.\n\n')


def print_functions_introduction(stdscr):
    print_logo(stdscr, 2)
    stdscr.addstr('Here is list of available functions.\n\n', curses.A_BOLD)

    stdscr.addstr('Use ')
    stdscr.addstr('ARROWS', curses.A_BOLD)
    stdscr.addstr(' on your keyboard for navigations.\n')
    stdscr.addstr('Press ')
    stdscr.addstr('ENTER', curses.A_BOLD)
    stdscr.addstr(' to confirm your choice.\n\n')

    stdscr.addstr('Press Q to get back to main menu...\n\n', curses.A_BOLD)
    stdscr.addstr('###################################\n\n', curses.A_BOLD)


def print_menu(stdscr, current_row_idx):
    stdscr.clear()

    print_introduction(stdscr)
    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            if row == 'Start\n':
                stdscr.addstr(f' > {row}', curses.color_pair(2))
            elif row == 'Documentation\n':
                stdscr.addstr(f' > {row}', curses.color_pair(4))
            elif row == 'Exit\n':
                stdscr.addstr(f' > {row}', curses.color_pair(3))
        else:
            if row == 'Start\n':
                stdscr.addstr(row, curses.color_pair(2))
            elif row == 'Documentation\n':
                stdscr.addstr(row, curses.color_pair(4))
            elif row == 'Exit\n':
                stdscr.addstr(row, curses.color_pair(3))

    stdscr.refresh()


def print_functions_menu(stdscr, pad_pos, current_row_idx, height, width):
    stdscr.clear()

    print_functions_introduction(stdscr)
    for idx, row in enumerate(AVAILABLE_FUNCTIONS):
        if idx == current_row_idx:
            stdscr.addstr(f' > {row}', curses.color_pair(1))
        else:
            stdscr.addstr(row)

    pad_refresh(stdscr, pad_pos, height, width)

