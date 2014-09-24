import os
import pytest

from pre_commit_hook.sort import main


base_dir = 'tests/resources'

def _create(path, content):
    with open(path, 'w') as f:
        f.write(content)

def create_correct_ordered_file(i):
    file_path = '{}/correct_{}.py'.format(base_dir, i)
    content = 'import json\nimport sys\n'
    _create(file_path, content)

def create_incorrectly_ordered_file(i):
    file_path = '{}/incorrect_{}.py'.format(base_dir, i)
    content = 'import sys\n\n\nimport json\n'
    _create(file_path, content)

def setup_function(function):
    create_correct_ordered_file(1)
    create_incorrectly_ordered_file(1)
    create_incorrectly_ordered_file(2)
    create_incorrectly_ordered_file(3)

def teardown_function(function):
    os.remove('{}/correct_1.py'.format(base_dir))
    os.remove('{}/incorrect_1.py'.format(base_dir))
    os.remove('{}/incorrect_2.py'.format(base_dir))
    os.remove('{}/incorrect_3.py'.format(base_dir))

@pytest.mark.parametrize(('args', 'expected_retval'), (
    (['tests/resources/correct_1.py'], 0),
    (['tests/resources/incorrect_1.py', '--diff-only'], 1),
    (['tests/resources/incorrect_2.py'], 1),
    (['tests/resources/incorrect_3.py', '--silent-overwrite'], 0),
))
def test_check_sort(args, expected_retval):
    assert main(args) == expected_retval
