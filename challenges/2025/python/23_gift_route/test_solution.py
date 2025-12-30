import pytest

from solution import min_steps_to_deliver


def test_min_steps_to_deliver_returns_int():
    map = [
        ['S', 'G']
    ]

    min_steps = min_steps_to_deliver(map)

    assert isinstance(min_steps, int)

@pytest.mark.parametrize(
    "map,expected_steps",
    [
        (
            [
                ['S', '.', 'G'],
                ['.', '#', '.'],
                ['G', '.', '.']
            ],
            4
        ),
        (
            [
                ['S', '#', 'G'],
                ['#', '#', '.'],
                ['G', '.', '.']
            ],
            -1
        ),
        (
            [
                ['S', 'G']
            ],
            1
        ),
        (
            [
                ['S', 'G', 'G', 'G']
            ],
            6
        ),
        (
            [
                ['S', '#'],
                ['.', '#'],
                ['.', '.'],
                ['G', '.']
            ],
            3
        )
    ]
)
def test_min_steps_to_deliver(map, expected_steps):
    min_steps = min_steps_to_deliver(map)

    assert min_steps == expected_steps
