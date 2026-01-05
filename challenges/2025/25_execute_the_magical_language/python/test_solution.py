import pytest

from solution import execute


def test_execute_returns_int():
    code = "+++"

    value = execute(code)

    assert isinstance(value, int)

@pytest.mark.parametrize(
    "code,expected_value",
    [
        pytest.param("+++", 3, id="test-2"),
        pytest.param("+--", -1, id="test-3"),
        pytest.param(">+++[-]", 0, id="test-4"),
        pytest.param(">>>+{++}", 3, id="test-5"),
        pytest.param("+{[-]}+", 1, id="test-6"),
        pytest.param("-[+>]++", 2, id="test-7"),
        pytest.param("-[+{++}]++{[-]}++", 2, id="test-8"),
        pytest.param("{+}{+}{+}", 0, id="test-9"),
        pytest.param("", 0, id="test-10"),
        pytest.param("+++{[-]+++[-]+}", 1, id="test-11"),
        pytest.param("{>++>++}", 0, id="test-12"),
        pytest.param("++++[-->]>++", 2, id="test-13")
    ]
)
def test_execute(code, expected_value):
    value = execute(code)

    assert value == expected_value
