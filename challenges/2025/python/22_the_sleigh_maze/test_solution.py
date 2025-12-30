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
        (
            [
                ['S', '.', '#', '.'],
                ['#', '.', '#', '.'],
                ['.', '.', '.', '.'],
                ['#', '#', '#', 'E']
            ],
            True
        ),
        (
            [
                ['S', '#', '#'],
                ['.', '#', '.'],
                ['.', '#', 'E']
            ],
            False
        ),
        (
            [
                ['S', 'E']
            ],
            True
        ),
        (
            [
                ['S', '#', 'E']
            ],
            False
        ),
        (
            [
                ['S', '.', '.'],
                ['#', '#', '.'],
                ['E', '.', '.']
            ],
            True
        ),
        (
            [
                ['S', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', 'E']
            ],
            True
        ),
        (
            [
                ['S', '.', '.', '.', '.'],
                ['#', '#', '#', '#', 'E']
            ],
            True
        )
    ]
)
def test_can_escape(maze, expected_value):
    output_value = can_escape(maze)

    assert output_value == expected_value
