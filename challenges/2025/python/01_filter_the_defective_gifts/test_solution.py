import pytest

from solution import filter_gifts


def test_filter_gifts_return_list():
    gifts = ["car", "ball"]

    non_defective_gifts = filter_gifts(gifts)

    assert isinstance(non_defective_gifts, list)

@pytest.mark.parametrize(
    "gifts,expected_gifts",
    [
        (["car", "doll#arm", "ball", "#train"], ["car", "ball"]),
        (["#broken", "#rusty"], []),
        ([], []),
        (["game", "poster", "sticker#bad", "console"], ["game", "poster", "console"]),
        (["#bad", "car", "#oops", "ball"], ["car", "ball"])
    ],
    ids=[
        "mixed_good_and_bad",
        "all_bad",
        "empty_list",
        "mixed_2",
        "bad_prefix_mixed"
    ]
)
def test_filter_gifts(gifts, expected_gifts):
    non_defective_gifts = filter_gifts(gifts)

    assert non_defective_gifts == expected_gifts
