from gendiff.formater.common import resolve_to_string


def format_plain(diff, path=''):
    result = []
    for item in diff:
        key = item['key']
        current_path = f'{path}.{key}' if path != '' else key
        lines = make_line(item, current_path)
        if lines != None:
            result.append(lines)
    return '\n'.join(result)


def make_line(item, path):
    status = item['status']
    if status == 'equal':
        return None
    elif status == 'nested':
        return format_plain(item['nested'], path)
    elif status == 'added':
        action = f'added with value: {get_value(item["new_value"])}'
    elif status == 'deleted':
        action = 'removed'
    elif status == 'changed':
        action = (f'updated. From {get_value(item["old_value"])}'
                  f' to {get_value(item["new_value"])}')
    else:
        raise ValueError('error in format diff')
    result = f"Property '{path}' was {action}"
    return result


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return resolve_to_string(value)
