def resolve_to_string(value):
    if value is None:
        result = 'null'
    elif isinstance(value, bool):
        result = 'false'
        if value:
            result = 'true'
    else:
        result = str(value)
    return result
