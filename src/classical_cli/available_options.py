import argparse

CLI_OPERATIONS = ['read', 'write', 'fetch', 'compile']


def setup_available_options(argv):
    parser = argparse.ArgumentParser(add_help=False)
    json_group = parser.add_argument_group('Read and write JSON file')
    web_group = parser.add_argument_group('Web')
    common_actions = parser.add_argument_group('Common actions')

    parser.add_argument('-h', '--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('-i', '--input-file',
                        metavar='',
                        help='Path to file to operate on.')
    parser.add_argument('-o', '--output-file',
                        metavar='',
                        help='Path and name of output file.')
    parser.add_argument('-u', '--url',
                        metavar='',
                        help='URL for the resource.')

    json_group.add_argument('-r', '--read',
                            action='store_true',
                            help='Convert your JSON data into Prolog program.')
    json_group.add_argument('-w', '--write',
                            action='store_true',
                            help='Convert your Prolog program into JSON data.')

    web_group.add_argument('-f', '--fetch',
                           action='store_true',
                           help='Fetch data from the web. Format is auto detected.')

    common_actions.add_argument('-c', '--compile',
                                action='store_true',
                                help='Compile and execute Prolog program.')

    return parser.parse_args(argv)
