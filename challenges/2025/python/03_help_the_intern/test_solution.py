import pytest

from solution import draw_gift


def test_draw_gift_returns_string():
    size = 2
    symbol = '#'

    gift = draw_gift(size, symbol)

    assert isinstance(gift, str)

@pytest.mark.parametrize(
    "size,symbol,expected_drawing", [
        (1, '+', ""),
        (2, '#', "##\n##"),
        (3, '#', "###\n# #\n###"),
        (4, '*', "****\n*  *\n*  *\n****"),
        (5, '@', "@@@@@\n@   @\n@   @\n@   @\n@@@@@")
    ]
)
def test_draw_gift(size, symbol, expected_drawing):
    gift = draw_gift(size, symbol)

    assert gift == expected_drawing
