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
        pytest.param(
            [
                {"toy": "car", "quantity": 3},
                {"toy": "doll", "quantity": 1},
                {"toy": "ball", "quantity": 2}
            ],
            ["car", "car", "car", "doll", "ball", "ball"],
            id="test-2"
        ),
        pytest.param(
            [
                {"toy": "train", "quantity": 0},
                {"toy": "bear", "quantity": -2},
                {"toy": "puzzle", "quantity": 1}
            ],
            ["puzzle"],
            id="test-3"
        ),
        pytest.param([], [], id="test-4"),
        pytest.param(
            [
                {"toy": "car", "quantity": 1},
                {"toy": "doll", "quantity": 2},
                {"toy": "ball", "quantity": 0},
                {"toy": "car", "quantity": 3}
            ],
            ["car", "doll", "doll", "car", "car", "car"],
            id="test-5"
        ),
        pytest.param(
            [
                {"toy": "robot", "quantity": 2},
                {"toy": "drone", "quantity": -3},
                {"toy": "ball", "quantity": 1}
            ],
            ["robot", "robot", "ball"],
            id="test-6"
        )
    ]
)
def test_manufacture_gifts(gifts_to_produce, expected_toys):
    toys_list = manufacture_gifts(gifts_to_produce)

    assert toys_list == expected_toys
