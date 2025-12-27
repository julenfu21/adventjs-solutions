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
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "U",
            "success"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RRRUU",
            "success"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "D",
            "fail"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "DD",
            "crash"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RU",
            "crash"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "UUU",
            "success"
        ),
        (
            dedent(
                """
                .....
                .*#.*
                .@...
                .....
                """
            ),
            "RR",
            "fail"
        ),
        (
            dedent(
                """
                .....
                .....
                .@..*
                .....
                """
            ),
            "RRRRRRRRR",
            "success"
        )
    ]
)
def test_move_reno(board, moves, expected_state):
    new_reno_state = move_reno(board, moves)

    assert new_reno_state == expected_state
