import pytest

from solution import filter_gifts


def test_filter_gifts_returns_list():
    gifts = ["car", "ball"]

    non_defective_gifts = filter_gifts(gifts)

    assert isinstance(non_defective_gifts, list)

@pytest.mark.parametrize(
    "gifts,expected_gifts",
    [
        pytest.param(["car", "doll#arm", "ball", "#train"], ["car", "ball"], id="test-2"),
        pytest.param(["#broken", "#rusty"], [], id="test-3"),
        pytest.param([], [], id="test-4"),
        pytest.param(["game", "poster", "sticker#bad", "console"], ["game", "poster", "console"], id="test-5"),
        pytest.param(["#bad", "car", "#oops", "ball"], ["car", "ball"], id="test-6")
    ]
)
def test_filter_gifts(gifts, expected_gifts):
    non_defective_gifts = filter_gifts(gifts)

    assert non_defective_gifts == expected_gifts
