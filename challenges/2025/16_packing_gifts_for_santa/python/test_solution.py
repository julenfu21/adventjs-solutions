import pytest

from solution import pack_gifts


def test_pack_gifts_returns_int():
    gifts = [2, 3, 4, 1]
    max_weight = 5

    sleigh_count = pack_gifts(gifts, max_weight)

    assert isinstance(sleigh_count, int)

@pytest.mark.parametrize(
    "gifts,max_weight,expected_count",
    [
        pytest.param([2, 3, 4, 1], 5, 2, id="test-2"),
        pytest.param([3, 3, 2, 1], 3, 3, id="test-3"),
        pytest.param([1, 1, 1, 1], 2, 2, id="test-4"),
        pytest.param([5, 6, 1], 5, None, id="test-5"),
        pytest.param([], 10, 0, id="test-6"),
        pytest.param([1, 2, 3, 4, 5], 10, 2, id="test-7"),
        pytest.param([5, 5, 5, 5], 5, 4, id="test-8"),
        pytest.param([1], 1, 1, id="test-9"),
        pytest.param([10], 5, None, id="test-10"),
        pytest.param([1, 2, 3], 6, 1, id="test-11"),
        pytest.param([3, 3, 3], 5, 3, id="test-12")
    ]
)
def test_pack_gifts(gifts, max_weight, expected_count):
    sleigh_count = pack_gifts(gifts, max_weight)

    assert sleigh_count == expected_count
