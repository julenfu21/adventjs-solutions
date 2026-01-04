from textwrap import dedent

import pytest

from solution import move_reno


def test_move_reno_returns_string():
    board = dedent(
        """
        .....
        .*#.*
        .@...
        .....
        """
    )
    moves = "U"

    new_reno_state = move_reno(board, moves)

    assert isinstance(new_reno_state, str)

@pytest.mark.parametrize(
    "board,moves,expected_state", [
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "U",
            "success",
            id="test-2"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RRRUU",
            "success",
            id="test-3"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "D",
            "fail",
            id="test-4"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "DD",
            "crash",
            id="test-5"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RU",
            "crash",
            id="test-6"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "UUU",
            "success",
            id="test-7"
        ),
        pytest.param(
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RR",
            "fail",
            id="test-8"
        ),
        pytest.param(
            dedent(
                """
                .....
                .....
                .@..*
                .....
                """
            ),
            "RRRRRRRRR",
            "success",
            id="test-9"
        )
    ]
)
def test_move_reno(board, moves, expected_state):
    new_reno_state = move_reno(board, moves)

    assert new_reno_state == expected_state
