import argparse

CLI_OPERATIONS = ['read', 'write', 'compile']


def setup_available_options(argv):
    parser = argparse.ArgumentParser(add_help=False)
    json_group = parser.add_argument_group('Read and write JSON file')
    common_actions = parser.add_argument_group('Common actions')

    parser.add_argument('-h', '--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('-i', '--input-file',
                        metavar='',
                        required=True,
                        help='Path to file to operate on.')
    parser.add_argument('-o', '--output-file',
                        metavar='',
                        required=True,
                        help='Path and name of output file.')

    json_group.add_argument('-r', '--read',
                            action='store_true',
                            help='Convert your JSON data into Prolog program.')
    json_group.add_argument('-w', '--write',
                            action='store_true',
                            help='Convert your Prolog program into JSON data.')

    common_actions.add_argument('-c', '--compile',
                                action='store_true',
                                help='Compile and execute Prolog program.')

    return parser.parse_args(argv)
