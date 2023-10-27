#!/usr/bin/env python3
from gendiff.formater.common import resolve_to_string

ONE_INDENT = '    '


def format_stylish(diff, level=1):
    result = []
    for item in diff:
        if not isinstance(item, dict):
            item = {'key': item, 'status': 'equal', 'old_value': diff[item]}
        result.extend(get_list_lines(item, level))
    return '{\n' + '\n'.join(result) + '\n' + get_indent(level - 1) + '}'


def get_list_lines(item, level):
    result = []
    status = item['status']
    key = item['key']
    indent = get_indent(level)
    if status == 'nested':
        result.append(f'{indent}{key}: '
                      f'{get_value(item["nested"], level)}')
    elif status == 'equal':
        result.append(f'{indent}{key}: '
                      f'{get_value(item["old_value"], level)}')
    elif status == 'deleted' or status == 'changed':
        result.append(f'{indent[:-2]}- {key}: '
                      f'{get_value(item["old_value"], level)}')
    if status == 'added' or status == 'changed':
        result.append(f'{indent[:-2]}+ {key}: '
                      f'{get_value(item["new_value"], level)}')
    return result


def get_value(value, level):
    if isinstance(value, (dict, list)):
        return format_stylish(value, level + 1)
    else:
        return resolve_to_string(value)


def get_indent(level):
    return ONE_INDENT * level
