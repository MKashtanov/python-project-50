#!/usr/bin/env python3
import json
import yaml
import os
from gendiff.comparator import create_diff
from gendiff.formater.stylish import format_stylish
from gendiff.formater.plain import format_plain
from gendiff.formater.json import format_json


def file_to_dict(path):
    result = {}
    if os.path.isfile(path):
        low_path = str(path).lower()
        if low_path[-5:] == '.json':
            result = json.load(open(path))
        if low_path[-5:] == '.yaml' or low_path[-4:] == '.yml':
            result = yaml.load(open(path), Loader=yaml.FullLoader)
    return result


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = file_to_dict(file_path1)
    dict2 = file_to_dict(file_path2)
    diff = create_diff(dict1, dict2)
    return get_formatted_diff(diff, format_name)


def get_formatted_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
