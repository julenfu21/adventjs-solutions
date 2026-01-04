import pytest

from solution import max_depth


def test_max_depth_returns_int():
    s = "[]"

    max_depth_level = max_depth(s)

    assert isinstance(max_depth_level, int)

@pytest.mark.parametrize(
    "s,expected_depth_level", [
        pytest.param("[]", 1, id="test-2"),
        pytest.param("[[]]", 2, id="test-3"),
        pytest.param("[][]", 1, id="test-4"),
        pytest.param("[[][]]", 2, id="test-5"),
        pytest.param("[[[]]]", 3, id="test-6"),
        pytest.param("[][[]][]", 2, id="test-7"),
        pytest.param("][", -1, id="test-8"),
        pytest.param("[[[", -1, id="test-9"),
        pytest.param("[]]]", -1, id="test-10"),
        pytest.param("[][][", -1, id="test-11")
    ]
)
def test_max_depth(s, expected_depth_level):
    max_depth_level = max_depth(s)

    assert max_depth_level == expected_depth_level
