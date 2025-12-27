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
        (
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
            ).rstrip()
        ),
        (
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
            ).rstrip()
        ),
        (
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
            ).rstrip()
        ),
        (
            1,
            'x',
            2,
            dedent(
                """\
                *
                #    
                """
            ).rstrip()
        ),
        (
            2,
            'o',
            2,
            dedent(
                """\
                 *
                o*o
                 #
                """
            ).rstrip()
        )
    ]
)
def test_match_gloves(height, ornament, frequency, expected_drawing):
    tree_drawing = draw_tree(height, ornament, frequency)

    assert tree_drawing == expected_drawing
