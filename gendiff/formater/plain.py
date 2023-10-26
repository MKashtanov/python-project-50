from gendiff.formater.common import resolve_to_string


def format_plain(diff):

    def inner(current_diff, path):
        result = []
        for item in current_diff:
            key = item["key"]
            current_path = f'{path}.{key}' if path != '' else key
            if item['status'] == 'equal':
                continue
            elif item['status'] == 'nested':
                nested = inner(item['nested'], current_path)
                if nested != '':
                    result.append(nested)
            elif item['status'] == 'different':
                action = ''
                keys = item.keys()
                if 'old_value' in keys and 'new_value' in keys:
                    action = (f'updated. From {get_value(item["old_value"])}'
                              f' to {get_value(item["new_value"])}')
                elif 'old_value' in keys:
                    action = 'removed'
                elif 'new_value' in keys:
                    action = f'added with value: {get_value(item["new_value"])}'
                result.append(f"Property '{current_path}' was {action}")
        return '\n'.join(result)

    return inner(diff, '')


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool) or value is None:
        return resolve_to_string(value)
    else:
        return f"'{value}'"
