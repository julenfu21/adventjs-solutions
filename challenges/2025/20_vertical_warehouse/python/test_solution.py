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
        pytest.param(
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
            ],
            id="test-2"
        ),
        pytest.param(
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
            ],
            id="test-3"
        ),
        pytest.param(
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
            ],
            id="test-4"
        ),
        pytest.param(
            [
                ['#', '.'],
                ['#', '.']
            ],
            [0],
            [
                ['#', '.'],
                ['#', '.']
            ],
            id="test-5"
        ),
        pytest.param(
            [
                ['.']
            ],
            [0],
            [
                ['#']
            ],
            id="test-6"
        ),
        pytest.param(
            [
                ['.', '.'],
                ['.', '.']
            ],
            [0, 0],
            [
                ['#', '.'],
                ['#', '.']
            ],
            id="test-7"
        )
    ]
)
def test_drop_gifts(warehouse, drops, expected_warehouse):
    new_warehouse = drop_gifts(warehouse, drops)

    assert new_warehouse == expected_warehouse
