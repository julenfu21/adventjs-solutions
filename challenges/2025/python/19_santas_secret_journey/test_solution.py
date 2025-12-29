import pytest

from solution import reveal_santa_route


def test_reveal_santa_route_returns_list():
    routes = [
        ["A", "B"]
    ]

    full_path = reveal_santa_route(routes)

    assert isinstance(full_path, list)

@pytest.mark.parametrize(
    "routes,expected_path",
    [
        (
            [
                ["MEX", "CAN"],
                ["UK", "GER"],
                ["CAN", "UK"]
            ],
            ["MEX", "CAN", "UK", "GER"]
        ),
        (
            [
                ["USA", "BRA"],
                ["JPN", "PHL"],
                ["BRA", "UAE"],
                ["UAE", "JPN"],
                ["CMX", "HKN"]
            ],
            ["USA", "BRA", "UAE", "JPN", "PHL"]
        ),
        (
            [
                ["STA", "HYD"],
                ["ESP", "CHN"]
            ],
            ["STA", "HYD"]
        ),
        (
            [
                ["A", "B"],
                ["C", "D"],
                ["E", "F"],
                ["G", "H"]
            ],
            ["A", "B"]
        )
    ]
)
def test_reveal_santa_route(routes, expected_path):
    full_path = reveal_santa_route(routes)

    assert full_path == expected_path
