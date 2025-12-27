import pytest

from solution import decode_santa_pin


def test_decode_santa_pin_returns_string():
    code = "[1++][2-][3+][<]"

    decoded_pin = decode_santa_pin(code)

    assert isinstance(decoded_pin, str)

@pytest.mark.parametrize(
    "code,expected_pin", [
        ("[1++][2-][3+][<]", "3144"),
        ("[9+][0-][4][<]", "0944"),
        ("[1+][2-]", None),
        ("[4][5++][6--][5++]", "4747"),
        ("[9+][0-][0-][8+]", "0999"),
        ("[0][<][<][<]", "0000"),
        ("[1+++++++++][2--][3----][<]", "0099")
    ]
)
def test_decode_santa_pin(code, expected_pin):
    decoded_pin = decode_santa_pin(code)

    assert decoded_pin == expected_pin
