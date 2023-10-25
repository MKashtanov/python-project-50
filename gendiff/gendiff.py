#!/usr/bin/env python3
import json
import yaml
import os
import gendiff.formater as Formater


def file_to_dict(path):
    result = {}
    if os.path.isfile(path):
        low_path = str(path).lower()
        if low_path[-5:] == '.json':
            result = json.load(open(path))
        if low_path[-5:] == '.yaml' or low_path[-4:] == '.yml':
            result = yaml.load(open(path), Loader=yaml.FullLoader)
    return result


def generate_diff(file_path1, file_path2, formater='stylish'):
    dict1 = file_to_dict(file_path1)
    dict2 = file_to_dict(file_path2)
    diff = create_diff(dict1, dict2)
    return get_diff_format(diff, formater)


def create_diff(tree1, tree2):
    result = []
    all_keys = list(set(tree1.keys()) | set(tree2.keys()))
    all_keys.sort()
    for key in all_keys:
        item = {'key': key}
        if key in tree1.keys() and key in tree2.keys():
            item.update(compare_values(tree1[key], tree2[key]))
        else:
            item['status'] = 'different'
            if key in tree1.keys():
                item['old_value'] = tree1[key]
            if key in tree2.keys():
                item['new_value'] = tree2[key]
        result.append(item)
    return result


def compare_values(value1, value2):
    result = {}
    if value1 == value2:
        result['status'] = 'equal'
        result['old_value'] = value1
    elif isinstance(value1, dict) and isinstance(value2, dict):
        result['status'] = 'nested'
        result['nested'] = create_diff(value1, value2)
    else:
        result['status'] = 'different'
        result['old_value'] = value1
        result['new_value'] = value2
    return result


def get_diff_format(diff, formater='stylish'):
    if formater == 'stylish':
        return Formater.format_stylish(diff)


# if __name__ == '__main__':
#    print(generate_diff(
#      '../tests/fixtures/file3.json', '../tests/fixtures/file4.json'))
