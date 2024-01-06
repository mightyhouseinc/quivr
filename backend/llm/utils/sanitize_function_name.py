import re


def sanitize_function_name(string):
    return re.sub(r"[^a-zA-Z0-9_-]", "", string)
