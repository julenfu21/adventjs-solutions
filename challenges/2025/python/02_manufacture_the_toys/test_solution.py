import pytest

from solution import manufacture_gifts


def test_manufacture_gifts_returns_list():
    gifts_to_produce = [
        {"toy": "car", "quantity": 1}
    ]

    toys_list = manufacture_gifts(gifts_to_produce)

    assert isinstance(toys_list, list)

@pytest.mark.parametrize(
    "gifts_to_produce,expected_toys",
    [
        (
            [
                {"toy": "car", "quantity": 3},
                {"toy": "doll", "quantity": 1},
                {"toy": "ball", "quantity": 2}
            ],
            ["car", "car", "car", "doll", "ball", "ball"]
        ),
        (
            [
                {"toy": "train", "quantity": 0},
                {"toy": "bear", "quantity": -2},
                {"toy": "puzzle", "quantity": 1}
            ],
            ["puzzle"]
        ),
        ([], []),
        (
            [
                {"toy": "car", "quantity": 1},
                {"toy": "doll", "quantity": 2},
                {"toy": "ball", "quantity": 0},
                {"toy": "car", "quantity": 3}
            ],
            ["car", "doll", "doll", "car", "car", "car"]
        ),
        (
            [
                {"toy": "robot", "quantity": 2},
                {"toy": "drone", "quantity": -3},
                {"toy": "ball", "quantity": 1}
            ],
            ["robot", "robot", "ball"]
        )
    ],
    ids=[
        "normal_case",
        "zero_and_negative_quantity",
        "empty_list",
        "mixed_quantities",
        "negative_quantity_filter"
    ]
)
def test_filter_gifts(gifts_to_produce, expected_toys):
    toys_list = manufacture_gifts(gifts_to_produce)

    assert toys_list == expected_toys
