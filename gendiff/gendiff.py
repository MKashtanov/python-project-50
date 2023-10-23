#!/usr/bin/env python3
import json
import yaml
import os


def file_to_dict(path):
    result = {}
    if os.path.isfile(path):
        low_path = str(path).lower()
        if low_path[-5:] == '.json':
            result = json.load(open(path))
        if low_path[-5:] == '.yaml' or low_path[-4:] == '.yml':
            result = yaml.load(open(path), Loader=yaml.FullLoader)
    return result


def generate_diff(file_path1, file_path2):
    result = []
    dict1 = file_to_dict(file_path1)
    dict2 = file_to_dict(file_path2)
    all_keys = list(set(dict1.keys()) | set(dict2.keys()))
    all_keys.sort()
    for key in all_keys:
        value1, value2 = dict1.get(key), dict2.get(key)
        if value1 == value2:
            result.append(f'    {key}: {value2}')
        else:
            if value1 is not None:
                result.append(f'  - {key}: {value1}')
            if value2 is not None:
                result.append(f'  + {key}: {value2}')
    return '{\n' + '\n'.join(result) + '\n}'
