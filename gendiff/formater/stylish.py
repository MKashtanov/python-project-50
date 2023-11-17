from gendiff.formater.common import resolve_to_string

ONE_INDENT = '    '


def format_stylish(diff, level=1):
    result = []
    for item in diff:
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
                      f'{get_value(old_value, level)}')
    elif status == 'deleted':
        result.append(f'{indent[:-2]}- {key}: '
                      f'{get_value(old_value, level)}')
    elif status == 'added':
        result.append(f'{indent[:-2]}+ {key}: '
                      f'{get_value(new_value, level)}')
    elif status == 'changed':
        result.append(f'{indent[:-2]}- {key}: '
                      f'{get_value(old_value, level)}')
        result.append(f'{indent[:-2]}+ {key}: '
                      f'{get_value(new_value, level)}')
    else:
        raise ValueError('error in format diff')
    return result


def get_value(value, level):
    if isinstance(value, dict):
        return dict_to_str(value, level)
    else:
        return resolve_to_string(value)


def dict_to_str(dict_, level):
    result = '{\n'
    for key in sorted(dict_.keys()):
        value = dict_[key]
        if isinstance(value, dict):
            line = dict_to_str(value, level + 1)
        else:
            line = resolve_to_string(value)
        result += f'{get_indent(level + 1)}{key}: {line}\n'
    result += get_indent(level) + '}'
    return result

def get_indent(level):
    return ONE_INDENT * level
