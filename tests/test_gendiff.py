from pathlib import Path
from gendiff.gendiff import generate_diff
import pytest


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name

test_data = [
    ('file1.json', 'file2.json', 'stylish', 'result_file1_file2'),
    ('file1.yml', 'file2.yml', 'stylish', 'result_file1_file2'),
    ('file3.json', 'file4.json', 'stylish', 'result_file3_file4'),
    ('file3.yml', 'file4.yml', 'stylish', 'result_file3_file4'),
    ('file3.json', 'file4.json', 'plain', 'result_file3_file4_plain'),
    ('file3.yml', 'file4.yml', 'plain', 'result_file3_file4_plain'),
    ]

@pytest.mark.parametrize('file1, file2, format_name, result_file', test_data)
def test_flat_json(file1, file2, format_name, result_file):
    result = open(get_path(result_file)).read()
    assert generate_diff(get_path(file1), get_path(file2), format_name) == result
