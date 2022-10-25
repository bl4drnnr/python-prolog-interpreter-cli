import re

PREDICATE_PATTERN = '[a-z]+[(]+[a-z,]+[)]+[.]'


def test_predicate(predicate):
    return re.match(PREDICATE_PATTERN, predicate)
