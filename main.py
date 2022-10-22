import sys

from curses import wrapper

from src.classical_cli.available_options import setup_available_options, CLI_OPERATIONS
from src.classical_cli.cli_execution import cli_execution
from src.classical_cli.exceptions import SingleArgument

from src.interactive_cli.init_curses_settings import init_curses_settings
from src.interactive_cli.menu import init_interactive_cli


def classical_cli(argv):
    options = setup_available_options(argv)
    operation = []
    set_options = {}

    for i in options.__dict__:
        if options.__dict__[i] is not None and options.__dict__[i]:
            if i in CLI_OPERATIONS:
                operation.append(i)
            else:
                set_options[i] = options.__dict__[i]

    try:
        if len(operation) != 1:
            raise SingleArgument
    except SingleArgument:
        print('One operation argument is expected.')
        sys.exit()

    cli_execution(operation[0], set_options)

    sys.exit()


def interactive_cli(stdscr):
    init_curses_settings()
    init_interactive_cli(stdscr)


def main(argv):
    if len(argv) > 0:
        classical_cli(argv)
    else:
        wrapper(interactive_cli)


if __name__ == '__main__':
    main(sys.argv[1:])
