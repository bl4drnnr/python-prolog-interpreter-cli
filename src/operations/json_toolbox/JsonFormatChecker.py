import json

from src.common.exceptions import WrongFactFormat, WrongJsonFormat
from src.common.variables import JSON_FORMAT_KEYS

from src.common.elements import *


def _check_item_type(item):
    if isinstance(item, list):
        return [_check_item_type(d) for d in item]
    elif item.get('type') == 'atom':
        return Atom(item.get('value'), item.get('data_type'))
    elif item.get('type') == 'list':
        if item.get('head') and item.get('tail'):
            return PList([], item.get('head'), item.get('tail'))
        else:
            return PList([_check_item_type(i) for i in item.get('items')])
    elif item.get('type') == 'predicate':
        return Predicate(item.get('name'), _parse_predicate(item))
    elif item.get('type') == 'condition':
        return Condition(item.get('left_side'), item.get('separator'), item.get('right_side'))
    elif item.get('type') == 'condition_statement':
        return ConditionStatement(
            _check_item_type(item.get('if_condition')),
            [_check_item_type(i) for i in item.get('then_clause')],
            [_check_item_type(i) for i in item.get('else_clause')]
        )


def _parse_predicate(predicate):
    return [_check_item_type(arg) for arg in predicate.get('arguments')]


def _parse_fact(fact):
    arguments = _parse_predicate(fact)
    conditions = [_check_item_type(condition) for condition in fact.get('conditions')]

    return [arguments, conditions]


class JsonFormatChecker:
    def __init__(self):
        self._parsed_data = {
            'predicates': [],
            'facts': []
        }

    def check_json_format(self, data):
        self._reset_data()
        self._check_items_format(data)
        return self._parsed_data

    def _reset_data(self):
        self._parsed_data = {
            'predicates': [],
            'facts': []
        }

    def _check_items_format(self, data):
        data = json.loads(data)
        if not data.get('data'):
            raise WrongJsonFormat(message="There no 'data' body.")

        data = data['data']

        for item in data:
            if item.get('type') is None:
                raise WrongJsonFormat(message=f"Wrong item format: {str(item)}")

            if item.get('type') not in JSON_FORMAT_KEYS:
                raise WrongJsonFormat(message=f"Wrong element name: {str(item)}")

            if item.get('type') == 'predicate':
                if item.get('arguments') is None or item.get('name') is None:
                    raise WrongJsonFormat(message=f"No name or arguments for predicate: {str(item)}")

                self._parsed_data.get('predicates').append(Predicate(item.get('name'), _parse_predicate(item)))

            elif item.get('type') == 'fact':
                if \
                        item.get('arguments') is None or \
                        item.get('conditions') is None or \
                        item.get('joins') is None or \
                        item.get('name') is None:
                    raise WrongFactFormat(message=f"Lack of required field for fact: {str(item)}")

                [arguments, conditions] = _parse_fact(item)
                self._parsed_data.get('facts').append(Fact(item.get('name'), arguments, item.get('joins'), conditions))
