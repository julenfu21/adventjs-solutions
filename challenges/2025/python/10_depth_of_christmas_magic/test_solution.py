import pytest

from solution import max_depth


def test_max_depth_returns_int():
    s = "[]"

    max_depth_level = max_depth(s)

    assert isinstance(max_depth_level, int)

@pytest.mark.parametrize(
    "s,expected_depth_level", [
        ("[]", 1),
        ("[[]]", 2),
        ("[][]", 1),
        ("[[][]]", 2),
        ("[[[]]]", 3),
        ("[][[]][]", 2),
        ("][", -1),
        ("[[[", -1),
        ("[]]]", -1),
        ("[][][", -1)
    ]
)
def test_move_reno(s, expected_depth_level):
    max_depth_level = max_depth(s)

    assert max_depth_level == expected_depth_level
