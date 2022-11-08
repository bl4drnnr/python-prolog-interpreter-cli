JSON_FORMAT = {
    "predicate": {
        "name": "str",
        "arguments": "list"
    },
    "fact": {
        "name": "str",
        "arguments": "list",
        "conditions": "list",
        "joins": "list"
    },
    "list": {
        "name": "str",
        "items": "list"
    }
}

ALLOWED_CONDITIONS_TYPES = ['predicate']
