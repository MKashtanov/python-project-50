import json
import yaml
from pathlib import Path
from gendiff.comparator import create_diff
from gendiff.formater.stylish import format_stylish
from gendiff.formater.plain import format_plain
from gendiff.formater.json import format_json


def get_data_from_file(path):
    f = open(path, 'r')
    data = f.read()
    return data


def data_to_dict(data, ext):
    if ext == '.json':
        result = json.loads(data)
    elif ext == '.yaml' or ext == '.yml':
        result = yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError('not support format file')
    return result


def file_to_dict(path):
    data = get_data_from_file(path)
    ext = Path(path).suffix
    return data_to_dict(data, ext)


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
    else:
        raise ValueError('not support formatted name')
