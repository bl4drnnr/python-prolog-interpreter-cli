def json_to_prolog(file_path):
    pass


def prolog_to_json(file_path):
    pass


def json_converter(operation_type, file_path):
    if operation_type == 'read':
        json_to_prolog(file_path)
    elif operation_type == 'write':
        prolog_to_json(file_path)
