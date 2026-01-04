import pytest

from solution import find_unsafe_gifts


def test_find_unsafe_gifts_returns_int():
    warehouse = [
        ".*.",
        "*#*",
        ".*."
    ]

    unsafe_gift_count = find_unsafe_gifts(warehouse)

    assert isinstance(unsafe_gift_count, int)

@pytest.mark.parametrize(
    "warehouse,expected_count", [
        pytest.param(
            [
                ".*.",
                "*#*",
                ".*."
            ],
            0,
            id="test-2"
        ),
        pytest.param(
            [
                "...",
                ".*.",
                "..."
            ],
            1,
            id="test-3"
        ),
        pytest.param(
            [
                "*.*",
                "...",
                "*#*"
            ],
            2,
            id="test-4"
        ),
        pytest.param(
            [
                ".....",
                ".*.*.",
                "..#..",
                ".*.*.",
                "....."
            ],
            4,
            id="test-5"
        ),
        pytest.param(
            [
                "#*.",
                "...",
                "..#"
            ],
            0,
            id="test-6"
        ),
        pytest.param(
            [
                "...#....",
                "..*#*..",
                "...#...."
            ],
            0,
            id="test-7"
        ),
        pytest.param(
            [
                "*.*",
                "...",
                "*.*"
            ],
            4,
            id="test-8"
        )
    ]
)
def test_find_unsafe_gifts(warehouse, expected_count):
    unsafe_gift_count = find_unsafe_gifts(warehouse)

    assert unsafe_gift_count == expected_count
