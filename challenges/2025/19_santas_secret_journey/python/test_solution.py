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
        pytest.param(
            [
                ["MEX", "CAN"],
                ["UK", "GER"],
                ["CAN", "UK"]
            ],
            ["MEX", "CAN", "UK", "GER"],
            id="test-2"
        ),
        pytest.param(
            [
                ["USA", "BRA"],
                ["JPN", "PHL"],
                ["BRA", "UAE"],
                ["UAE", "JPN"],
                ["CMX", "HKN"]
            ],
            ["USA", "BRA", "UAE", "JPN", "PHL"],
            id="test-3"
        ),
        pytest.param(
            [
                ["STA", "HYD"],
                ["ESP", "CHN"]
            ],
            ["STA", "HYD"],
            id="test-4"
        ),
        pytest.param(
            [
                ["A", "B"],
                ["C", "D"],
                ["E", "F"],
                ["G", "H"]
            ],
            ["A", "B"],
            id="test-5"
        )
    ]
)
def test_reveal_santa_route(routes, expected_path):
    full_path = reveal_santa_route(routes)

    assert full_path == expected_path
