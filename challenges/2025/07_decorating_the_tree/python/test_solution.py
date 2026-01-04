from textwrap import dedent

import pytest

from solution import draw_tree


def test_draw_tree_returns_string():
    height = 3
    ornament = 'o'
    frequency = 2

    tree_drawing = draw_tree(height, ornament, frequency)

    assert isinstance(tree_drawing, str)

@pytest.mark.parametrize(
    "height,ornament,frequency,expected_drawing", [
        pytest.param(
            5,
            'o',
            2,
            dedent(
                """\
                    *
                   o*o
                  *o*o*
                 o*o*o*o
                *o*o*o*o*
                    #
                """
            ).rstrip(),
            id="test-2"
        ),
        pytest.param(
            3,
            '@',
            3,
            dedent(
                """\
                  *
                 *@*
                *@**@
                  #
                """
            ).rstrip(),
            id="test-3"
        ),
        pytest.param(
            4,
            '+',
            1,
            dedent(
                """\
                   +
                  +++
                 +++++
                +++++++
                   #
                """
            ).rstrip(),
            id="test-4"
        ),
        pytest.param(
            1,
            'x',
            2,
            dedent(
                """\
                *
                #    
                """
            ).rstrip(),
            id="test-5"
        ),
        pytest.param(
            2,
            'o',
            2,
            dedent(
                """\
                 *
                o*o
                 #
                """
            ).rstrip(),
            id="test-6"
        )
    ]
)
def test_draw_tree(height, ornament, frequency, expected_drawing):
    tree_drawing = draw_tree(height, ornament, frequency)

    assert tree_drawing == expected_drawing
