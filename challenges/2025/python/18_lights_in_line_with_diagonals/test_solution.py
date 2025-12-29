import pytest

from solution import has_four_in_a_row


def test_has_four_in_a_row_returns_boolean():
    board = [
        ['R', '.', '.', '.'],
        ['.', 'R', '.', '.'],
        ['.', '.', 'R', '.'],
        ['.', '.', '.', 'R']
    ]

    check_result = has_four_in_a_row(board)

    assert isinstance(check_result, bool)

@pytest.mark.parametrize(
    "board,expected_result",
    [
        (
            [
                ['R', '.', '.', '.'],
                ['.', 'R', '.', '.'],
                ['.', '.', 'R', '.'],
                ['.', '.', '.', 'R']
            ],
            True
        ),
        (
            [
                ['.', '.', '.', 'G'],
                ['.', '.', 'G', '.'],
                ['.', 'G', '.', '.'],
                ['G', '.', '.', '.']
            ],
            True
        ),
        (
            [
                ['R', 'R', 'R', 'R'],
                ['G', 'G', '.', '.'],
                ['.', '.', '.', '.'],
                ['.', '.', '.', '.']
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
                ['.', 'G', '.'],
                ['.', 'G', '.'],
                ['.', 'G', '.'],
                ['.', 'G', '.']
            ],
            True
        )
    ]
)
def test_has_four_in_a_row(board, expected_result):
    check_result = has_four_in_a_row(board)

    assert check_result == expected_result
