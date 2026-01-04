from textwrap import dedent

import pytest

from solution import draw_gift


def test_draw_gift_returns_string():
    size = 2
    symbol = '#'

    gift = draw_gift(size, symbol)

    assert isinstance(gift, str)

@pytest.mark.parametrize(
    "size,symbol,expected_drawing", [
        pytest.param(1, '+', "", id="test-2"),
        pytest.param(
            2,
            '#',
            dedent(
                """\
                ##
                ##
                """
            ).rstrip(),
            id="test-3"
        ),
        pytest.param(
            3,
            '#',
            dedent(
                """\
                ###
                # #
                ###
                """
            ).rstrip(),
            id="test-4"
        ),
        pytest.param(
            4,
            '*',
            dedent(
                """\
                ****
                *  *
                *  *
                ****
                """
            ).rstrip(),
            id="test-5"
        ),
        pytest.param(
            5,
            '@',
            dedent(
                """\
                @@@@@
                @   @
                @   @
                @   @
                @@@@@
                """
            ).rstrip(),
            id="test-6"
        )
    ]
)
def test_draw_gift(size, symbol, expected_drawing):
    gift = draw_gift(size, symbol)

    assert gift == expected_drawing
