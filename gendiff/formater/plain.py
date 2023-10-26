#!/usr/bin/env python3
from gendiff.formater.common import resolve_to_string


def format_plain(diff, path=''):
    result = []
    for item in diff:
        key = item['key']
        current_path = f'{path}.{key}' if path != '' else key
        if item['status'] == 'nested':
            lines = format_plain(item['nested'], current_path)
        else:
            lines = make_line(item, current_path)
        if lines != '':
            result.append(lines)
    return '\n'.join(result)


def make_line(item, path):
    action = ''
    status = item['status']
    if status == 'added':
        action = f'added with value: {get_value(item["new_value"])}'
    elif status == 'deleted':
        action = 'removed'
    elif status == 'changed':
        action = (f'updated. From {get_value(item["old_value"])}'
                  f' to {get_value(item["new_value"])}')
    result = '' if action == '' else f"Property '{path}' was {action}"
    return result


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool) or value is None:
        return resolve_to_string(value)
    else:
        return f"'{value}'"