import pytest
from isort.isort import stdout

from pre_commit_hook.sort import main


def write_file(filename, contents):
    with open(filename, 'w') as file_obj:
        file_obj.write(contents)


@pytest.fixture
def tmpfiles(tmpdir):
    write_file(tmpdir.join('correct_1.py').strpath, 'import json\nimport sys\n')
    write_file(tmpdir.join('incorrect_1.py').strpath, 'import sys\n\n\nimport json\n')
    write_file(tmpdir.join('incorrect_2.py').strpath, 'import sys\n\n\nimport json\n')
    return tmpdir


def test_sort(tmpfiles):    
    assert main([tmpfiles.join('correct_1.py').strpath]) == 0
    assert main([tmpfiles.join('incorrect_1.py').strpath]) == 1
    assert main([tmpfiles.join('incorrect_2.py').strpath, '--check-only']) == 1
    assert main([tmpfiles.join('incorrect_2.py').strpath, '--silent-overwrite']) == 0


def test_sort_with_diff(tmpfiles):
    filename = tmpfiles.join('incorrect_1.py').strpath
    main(['--diff', '--check-only', filename])

    stdout.seek(0)
    lines = stdout.read().splitlines()
    # Skip diff header
    lines = lines[4:]
    assert lines == [
        '+import json',
        ' import sys',
        '-',
        '-',
        '-import json',
    ]
