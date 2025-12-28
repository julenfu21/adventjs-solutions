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
        ([2, 3, 4, 1], 5, 2),
        ([3, 3, 2, 1], 3, 3),
        ([1, 1, 1, 1], 2, 2),
        ([5, 6, 1], 5, None),
        ([], 10, 0),
        ([1, 2, 3, 4, 5], 10, 2),
        ([5, 5, 5, 5], 5, 4),
        ([1], 1, 1),
        ([10], 5, None),
        ([1, 2, 3], 6, 1),
        ([3, 3, 3], 5, 3)
    ]
)
def test_pack_gifts(gifts, max_weight, expected_count):
    sleigh_count = pack_gifts(gifts, max_weight)

    assert sleigh_count == expected_count
