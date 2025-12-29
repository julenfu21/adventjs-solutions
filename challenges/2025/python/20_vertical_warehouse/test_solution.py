import pytest

from solution import drop_gifts


def test_drop_gifts_returns_list():
    warehouse = [
        ['.', '.']
    ]
    drops = [0]

    new_warehouse = drop_gifts(warehouse, drops)

    assert isinstance(new_warehouse, list)

@pytest.mark.parametrize(
    "warehouse,drops,expected_warehouse",
    [
        (
            [
                ['.', '.', '.'],
                ['.', '#', '.'],
                ['#', '#', '.']
            ],
            [0],
            [
                ['.', '.', '.'],
                ['#', '#', '.'],
                ['#', '#', '.']
            ]
        ),
        (
            [
                ['.', '.', '.'],
                ['#', '#', '.'],
                ['#', '#', '#']
            ],
            [0, 2],
            [
                ['#', '.', '.'],
                ['#', '#', '#'],
                ['#', '#', '#']
            ]
        ),
        (
            [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']
            ],
            [0, 1, 2],
            [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['#', '#', '#']
            ]
        ),
        (
            [
                ['#', '.'],
                ['#', '.']
            ],
            [0],
            [
                ['#', '.'],
                ['#', '.']
            ]
        ),
        (
            [
                ['.']
            ],
            [0],
            [
                ['#']
            ]
        ),
        (
            [
                ['.', '.'],
                ['.', '.']
            ],
            [0, 0],
            [
                ['#', '.'],
                ['#', '.']
            ]
        )
    ]
)
def test_drop_gifts(warehouse, drops, expected_warehouse):
    new_warehouse = drop_gifts(warehouse, drops)

    assert new_warehouse == expected_warehouse
