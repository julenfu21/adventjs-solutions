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
        pytest.param(
            [
                ['R', '.', '.', '.'],
                ['.', 'R', '.', '.'],
                ['.', '.', 'R', '.'],
                ['.', '.', '.', 'R']
            ],
            True,
            id="test-2"
        ),
        pytest.param(
            [
                ['.', '.', '.', 'G'],
                ['.', '.', 'G', '.'],
                ['.', 'G', '.', '.'],
                ['G', '.', '.', '.']
            ],
            True,
            id="test-3"
        ),
        pytest.param(
            [
                ['R', 'R', 'R', 'R'],
                ['G', 'G', '.', '.'],
                ['.', '.', '.', '.'],
                ['.', '.', '.', '.']
            ],
            True,
            id="test-4"
        ),
        pytest.param(
            [
                ['R', 'G', 'R'],
                ['G', 'R', 'G'],
                ['G', 'R', 'G']
            ],
            False,
            id="test-5"
        ),
        pytest.param(
            [
                ['.', 'G', '.'],
                ['.', 'G', '.'],
                ['.', 'G', '.'],
                ['.', 'G', '.']
            ],
            True,
            id="test-6"
        )
    ]
)
def test_has_four_in_a_row(board, expected_result):
    check_result = has_four_in_a_row(board)

    assert check_result == expected_result
