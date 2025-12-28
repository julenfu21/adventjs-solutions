import pytest

from solution import has_four_lights


def test_has_four_lights_returns_boolean():
    board = [
        ['.', '.', '.', '.'],
        ['R', 'R', 'R', 'R']
    ]

    check_result = has_four_lights(board)

    assert isinstance(check_result, bool)

@pytest.mark.parametrize(
    "board,expected_result",
    [
        (
            [
                ['.', '.', '.', '.', '.'],
                ['R', 'R', 'R', 'R', '.'],
                ['G', 'G', '.', '.', '.']
            ],
            True
        ),
        (
            [
                ['.', 'G', '.', '.'],
                ['.', 'G', '.', '.'],
                ['.', 'G', '.', '.'],
                ['.', 'G', '.', '.']
            ],
            True
        ),
        (
            [
                ['R', 'G', 'R'],
                ['G', 'R', 'G'],
                ['G', 'R', 'G']
            ],
            False
        ),
        (
            [
                ['R', 'R', 'R', '.'],
                ['.', '.', '.', '.']
            ],
            False
        ),
        (
            [
                ['.', '.', 'R', 'R', 'R', 'R'],
                ['.', '.', '.', '.', '.', '.']
            ],
            True
        ),
        (
            [
                ['.', '.', '.', '.'],
                ['.', '.', '.', '.']
            ],
            False
        ),
        (
            [
                ['G', 'G', 'G', 'G', 'G']
            ],
            True
        )
    ]
)
def test_has_four_lights(board, expected_result):
    check_result = has_four_lights(board)

    assert check_result == expected_result
