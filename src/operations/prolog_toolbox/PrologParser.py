from src.common.elements import *


def _check_item_type(item):
    if isinstance(item, Atom):
        return {
            "type": item.type,
            "data_type": item.data_type,
            "value": int(item.atom) if item.data_type == 'number' else item.atom
        }
    elif isinstance(item, PList):
        if item.head and item.tail:
            return {
                "type": item.type,
                "head": item.head.atom,
                "tail": item.tail.atom
            }
        else:
            return {
                "type": item.type,
                "items": _parse_predicate_arguments(item.items)
            }
    elif isinstance(item, Predicate):
        return {
            "type": item.type,
            "name": item.name,
            "arguments": _parse_condition_items(item)
        }
    elif isinstance(item, Condition):
        return {
            "type": item.type,
            "right_side": item.right_side,
            "separator": item.separator,
            "left_side": item.left_side
        }


def _parse_predicate_arguments(arguments):
    iter_items = arguments if isinstance(arguments, list) else arguments.items
    return [_check_item_type(arg) for arg in iter_items]


def _parse_condition_items(condition):
    return [_check_item_type(predicate_item) for predicate_item in condition.arguments.items]


def _parse_predicate(predicate):
    return {
        "type": predicate.type,
        "name": predicate.name,
        "arguments": _parse_condition_items(predicate)
    }


def _parse_condition(condition):
    return {
        "type": condition.type,
        "right_side": condition.right_side,
        "left_side": condition.left_side,
        "separator": condition.separator
    }


def _parse_condition_statement(condition_statement):
    return {
        "type": "condition_statement",
        "if_condition": _check_item_type(condition_statement.if_condition),
        "then_clause": [_check_item_type(item) for item in condition_statement.then_clause],
        "else_clause": [_check_item_type(item) for item in condition_statement.else_clause]
    }


class PrologParser:
    def __init__(self):
        self._output_json = []

    def parse_prolog(self, prolog_data):
        self._reset_data()

        for item in prolog_data:
            if item.type == 'predicate':
                self._output_json.append({
                    "type": item.type,
                    "name": item.name,
                    "arguments": _parse_predicate_arguments(item.arguments)
                })
            elif item.type == 'fact':
                conditions = []

                for condition in item.conditions:
                    if isinstance(condition, Predicate):
                        conditions.append(_parse_predicate(condition))
                    elif isinstance(condition, Condition):
                        conditions.append(_parse_condition(condition))
                    elif isinstance(condition, ConditionStatement):
                        conditions.append(_parse_condition_statement(condition))

                self._output_json.append({
                    "type": item.type,
                    "name": item.arguments.name,
                    "arguments": _parse_predicate_arguments(item.arguments.arguments),
                    "joins": item.joins,
                    "conditions": conditions
                })

        return self._output_json

    def _reset_data(self):
        self._output_json = []
