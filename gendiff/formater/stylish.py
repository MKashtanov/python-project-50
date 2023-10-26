#!/usr/bin/env python3
from gendiff.formater.common import resolve_to_string

SEPARATOR = '    '


def format_stylish(diff, level=1):
    result = []
    separator = get_full_separator(level)
    if isinstance(diff, list):
        for item in diff:
            result.extend(make_lines(item, level))
    elif isinstance(diff, dict):
        '''item = [{'status': 'nested', 'nested' diff}]
        result.extend(make_lines(item, level))'''

        for key in sorted(list(diff.keys())):
            value = diff.get(key)
            if isinstance(value, dict):
                result.append(
                    f'{separator}{key}: {format_stylish(value, level + 1)}'
                )
            else:
                result.append(f'{separator}{key}: {value}')
    return ('{\n' + '\n'.join(result) + '\n' +
            get_full_separator(level - 1) + '}')


def make_lines(item, level):
    result = []
    status = item['status']
    key = item['key']
    separator = get_full_separator(level)
    if status == 'nested':
        result.append(f'{separator}{key}: '
                      f'{make_stylish_line(item["nested"], level)}')
    elif status == 'equal':
        result.append(f'{separator}{key}: '
                      f'{make_stylish_line(item["old_value"], level)}')
    if status == 'deleted' or status == 'changed':
        result.append(f'{separator[:-2]}- {key}: '
                      f'{make_stylish_line(item["old_value"], level)}')
    if status == 'added' or status == 'changed':
        result.append(f'{separator[:-2]}+ {key}: '
                      f'{make_stylish_line(item["new_value"], level)}')
    return result


def get_full_separator(level):
    return SEPARATOR * level


def make_stylish_line(value, level):
    if isinstance(value, (dict, list)):
        return format_stylish(value, level + 1)
    else:
        return resolve_to_string(value)
