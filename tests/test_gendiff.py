from pathlib import Path
from gendiff.scripts.gendiff import generate_diff
import pytest


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name

test_data = [
    ('file1.json', 'file2.json', 'result_file1_file2'),
    ]

@pytest.mark.parametrize('file1, file2, result_file', test_data)
def test_flat_json(file1, file2, result_file):
    result = open(get_path(result_file)).read()
    assert generate_diff(get_path(file1), get_path(file2)) == result