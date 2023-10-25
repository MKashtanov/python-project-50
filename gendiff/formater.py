SEPARATOR = '    '


def format_stylish(diff):

    def inner(current_diff, level):
        result = []
        separator = get_full_separator(level)
        if isinstance(current_diff, list):
            for item in current_diff:
                if item['status'] == 'nested':
                    result.append(f'{separator}{item["key"]}: {inner(item["nested"], level + 1)}')
                elif item['status'] == 'equal':
                    result.append(f'{separator}{item["key"]}: {item["old_value"]}')
                elif item['status'] == 'different':
                    if 'old_value' in item.keys():
                        if isinstance(item.get('old_value'), dict):
                            result.append(f'{separator[:-2]}- {item["key"]}: {inner(item.get("old_value"), level + 1)}')
                        else:
                            result.append(f'{separator[:-2]}- {item["key"]}: {resolve_to_string(item.get("old_value"))}')
                    if 'new_value' in item.keys():
                        if isinstance(item.get('new_value'), dict):
                            result.append(f'{separator[:-2]}+ {item["key"]}: {inner(item.get("new_value"), level + 1)}')
                        else:
                            result.append(f'{separator[:-2]}+ {item["key"]}: {resolve_to_string(item.get("new_value"))}')
        elif isinstance(current_diff, dict):
            for key in sorted(list(current_diff.keys())):
                value = current_diff.get(key)
                if isinstance(value, dict):
                    result.append(f'{separator}{key}: {inner(value, level + 1)}')
                else:
                    result.append(f'{separator}{key}: {value}')
        return '{\n' + '\n'.join(result) + '\n' + get_full_separator(level - 1) + '}'

    return inner(diff, 1)


def get_full_separator(level):
    return SEPARATOR * level


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
