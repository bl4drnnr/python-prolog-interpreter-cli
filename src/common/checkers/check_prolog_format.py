from src.common.checkers.rules_prolog_format import test_predicate, test_fact
from src.common.exceptions import WrongPrologFormat


def check_prolog_format(data):
    filtered_data = []

    for row in data:
        filtered_data.append(row.replace(" ", ""))

    print(filtered_data)
