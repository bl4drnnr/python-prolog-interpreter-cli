from src.common.checkers.rules_json_format import JSON_FORMAT, ALLOWED_CONDITIONS_TYPES
from src.common.exceptions import WrongJsonFormat, WrongFactFormat


def check_json_format(data):
    predicates = []
    facts = []

    for key, value in data.items():
        if key not in JSON_FORMAT:
            raise WrongJsonFormat
        else:
            for item_key, item_value in value.items():

                if item_key not in JSON_FORMAT[key]:
                    raise WrongJsonFormat
                if type(item_value).__name__ != JSON_FORMAT[key][item_key]:
                    raise WrongJsonFormat

        if key == 'predicate':
            predicates.append(value)

        elif key == 'fact':

            if len(value['conditions']) == 0:
                raise WrongFactFormat

            if 'arguments' not in value or type(value['arguments']).__name__ != 'list':
                raise WrongFactFormat

            if \
                    "joins" not in value or \
                    type(value['joins']).__name__ != 'list' or \
                    len(value['joins']) != len(value['conditions']) - 1:
                raise WrongFactFormat

            for condition in value['conditions']:
                if 'type' not in condition:
                    raise WrongFactFormat
                if condition['type'] not in ALLOWED_CONDITIONS_TYPES:
                    raise WrongFactFormat
                if condition['type'] == 'predicate':
                    if 'arguments' not in condition or type(condition['arguments']).__name__ != 'list':
                        raise WrongFactFormat

            facts.append(value)

    return {
        'predicates': predicates,
        'facts': facts
    }
