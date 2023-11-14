from gendiff.formater.common import resolve_to_string

ONE_INDENT = '    '


def format_stylish(diff, level=1):
    result = []
    for item in diff:
        print(f'item={item}')
        if not isinstance(item, dict):
            item = {'key': item, 'status': 'equal', 'old_value': diff[item]}
        result.extend(get_list_lines(item, level))
    result.insert(0, '{')
    result.append(get_indent(level - 1) + '}')
    return '\n'.join(result)


def get_list_lines(item, level):
    result = []
    status = item['status']
    key = item['key']
    new_value = item.get('new_value')
    old_value = item.get('old_value')

    indent = get_indent(level)
    if status == 'nested':
        result.append(f'{indent}{key}: '
                      f'{format_stylish(item["nested"], level+1)}')
    elif status == 'equal':
        result.append(f'{indent}{key}: '
                      f'{resolve_to_string(old_value)}')
    elif status == 'deleted':
        result.append(f'{indent[:-2]}- {key}: '
                      f'{resolve_to_string(old_value)}')
    elif status == 'added':
        result.append(f'{indent[:-2]}+ {key}: '
                      f'{resolve_to_string(new_value)}')
    elif status == 'changed':
        result.append(f'{indent[:-2]}- {key}: '
                      f'{resolve_to_string(old_value)}')
        result.append(f'{indent[:-2]}+ {key}: '
                      f'{resolve_to_string(new_value)}')
    else:
        raise ValueError('error in format diff')
    return result


def get_indent(level):
    return ONE_INDENT * level
