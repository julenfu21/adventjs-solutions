import pytest

from solution import clear_gifts


def test_clear_gifts_returns_list():
    warehouse = [
        ['.', '.']
    ]
    drops = [0]

    new_warehouse = clear_gifts(warehouse, drops)

    assert isinstance(new_warehouse, list)

@pytest.mark.parametrize(
    "warehouse,drops,expected_warehouse",
    [
        (
            [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['#', '.', '#']
            ],
            [1],
            [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']
            ]
        ),
        (
            [
                ['.', '.', '#'],
                ['#', '.', '#'],
                ['#', '.', '#']
            ],
            [0, 1, 2],
            [
                ['.', '.', '#'],
                ['#', '.', '#'],
                ['#', '.', '#']
            ]
        ),
        (
            [
                ['.', '.', '.'],
                ['#', '#', '.'],
                ['#', '#', '.']
            ],
            [2, 2],
            [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']
            ]
        ),
        (
            [
                ['.', '.'],
                ['.', '.']
            ],
            [1, 1],
            [
                ['.', '#'],
                ['.', '#']
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
        )
    ]
)
def test_clear_gifts(warehouse, drops, expected_warehouse):
    new_warehouse = clear_gifts(warehouse, drops)

    assert new_warehouse == expected_warehouse
