import pytest

from pre_commit_hook.sort import main


@pytest.mark.parametrize(('args', 'expected_retval'), (
    (['tests/resources/correct_order.py'], 0),
    (['tests/resources/incorrect_order.py', '--diff-only'], 1),
))
def test_check_sort(args, expected_retval):
    assert main(args) == expected_retval
