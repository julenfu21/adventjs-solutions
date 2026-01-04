import pytest

from solution import decode_santa_pin


def test_decode_santa_pin_returns_string():
    code = "[1++][2-][3+][<]"

    decoded_pin = decode_santa_pin(code)

    assert isinstance(decoded_pin, str)

@pytest.mark.parametrize(
    "code,expected_pin", [
        pytest.param("[1++][2-][3+][<]", "3144", id="test-2"),
        pytest.param("[9+][0-][4][<]", "0944", id="test-3"),
        pytest.param("[1+][2-]", None, id="test-4"),
        pytest.param("[4][5++][6--][5++]", "4747", id="test-5"),
        pytest.param("[9+][0-][0-][8+]", "0999", id="test-6"),
        pytest.param("[0][<][<][<]", "0000", id="test-7"),
        pytest.param("[1+++++++++][2--][3----][<]", "0099", id="test-8")
    ]
)
def test_decode_santa_pin(code, expected_pin):
    decoded_pin = decode_santa_pin(code)

    assert decoded_pin == expected_pin
