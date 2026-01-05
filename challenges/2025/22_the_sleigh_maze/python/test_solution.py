import pytest

from solution import can_escape


def test_can_escape_returns_boolean():
    maze = [
        ['S', 'E']
    ]

    output_value = can_escape(maze)

    assert isinstance(output_value, bool)

@pytest.mark.parametrize(
    "maze,expected_value",
    [
        pytest.param(
            [
                ['S', '.', '#', '.'],
                ['#', '.', '#', '.'],
                ['.', '.', '.', '.'],
                ['#', '#', '#', 'E']
            ],
            True,
            id="test-2"
        ),
        pytest.param(
            [
                ['S', '#', '#'],
                ['.', '#', '.'],
                ['.', '#', 'E']
            ],
            False,
            id="test-3"
        ),
        pytest.param(
            [
                ['S', 'E']
            ],
            True,
            id="test-4"
        ),
        pytest.param(
            [
                ['S', '#', 'E']
            ],
            False,
            id="test-5"
        ),
        pytest.param(
            [
                ['S', '.', '.'],
                ['#', '#', '.'],
                ['E', '.', '.']
            ],
            True,
            id="test-6"
        ),
        pytest.param(
            [
                ['S', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', 'E']
            ],
            True,
            id="test-7"
        ),
        pytest.param(
            [
                ['S', '.', '.', '.', '.'],
                ['#', '#', '#', '#', 'E']
            ],
            True,
            id="test-8"
        )
    ]
)
def test_can_escape(maze, expected_value):
    output_value = can_escape(maze)

    assert output_value == expected_value
