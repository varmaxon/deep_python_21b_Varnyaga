from typing import Callable
import json


def parse_json(json_str: str,
               required_fields=None,
               keywords=None,
               keyword_callback: Callable = None):

    if not (isinstance(json_str, str) and
            required_fields and keywords and keyword_callback):
        return -1

    json_doc = json.loads(json_str)

    keys = json_doc.keys() & required_fields
    for key in keys:
        values = set(json_doc.get(key).split()) & set(keywords)
        for value in values:
            keyword_callback(key, value)

    return 0
