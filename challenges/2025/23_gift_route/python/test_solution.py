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
        pytest.param(
            [
                ['S', '.', 'G'],
                ['.', '#', '.'],
                ['G', '.', '.']
            ],
            4,
            id="test-2"
        ),
        pytest.param(
            [
                ['S', '#', 'G'],
                ['#', '#', '.'],
                ['G', '.', '.']
            ],
            -1,
            id="test-3"
        ),
        pytest.param(
            [
                ['S', 'G']
            ],
            1,
            id="test-4"
        ),
        pytest.param(
            [
                ['S', 'G', 'G', 'G']
            ],
            6,
            id="test-5"
        ),
        pytest.param(
            [
                ['S', '#'],
                ['.', '#'],
                ['.', '.'],
                ['G', '.']
            ],
            3,
            id="test-6"
        )
    ]
)
def test_min_steps_to_deliver(map, expected_steps):
    min_steps = min_steps_to_deliver(map)

    assert min_steps == expected_steps
