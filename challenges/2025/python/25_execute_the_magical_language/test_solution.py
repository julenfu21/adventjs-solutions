import pytest

from solution import execute


def test_execute_returns_int():
    code = "+++"

    value = execute(code)

    assert isinstance(value, int)

@pytest.mark.parametrize(
    "code,expected_value",
    [
        ("+++", 3),
        ("+--", -1),
        (">+++[-]", 0),
        (">>>+{++}", 3),
        ("+{[-]}+", 1),
        ("-[+>]++", 2),
        ("-[+{++}]++{[-]}++", 2),
        ("{+}{+}{+}", 0),
        ("", 0),
        ("+++{[-]+++[-]+}", 1),
        ("{>++>++}", 0),
        ("++++[-->]>++", 2)
    ]
)
def test_execute(code, expected_value):
    value = execute(code)

    assert value == expected_value
