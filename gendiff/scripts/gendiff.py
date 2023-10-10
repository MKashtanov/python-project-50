#!/usr/bin/env python3
import argparse
import json


def generate_diff(file_path1, file_path2):
    result = []
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
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


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(f'diff={diff}')

    print(f'args={args}')


if __name__ == '__main__':
    main()
