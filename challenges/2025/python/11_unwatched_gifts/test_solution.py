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
        (
            [
                ".*.",
                "*#*",
                ".*."
            ],
            0
        ),
        (
            [
                "...",
                ".*.",
                "..."
            ],
            1
        ),
        (
            [
                "*.*",
                "...",
                "*#*"
            ],
            2
        ),
        (
            [
                ".....",
                ".*.*.",
                "..#..",
                ".*.*.",
                "....."
            ],
            4
        ),
        (
            [
                "#*.",
                "...",
                "..#"
            ],
            0
        ),
        (
            [
                "...#....",
                "..*#*..",
                "...#...."
            ],
            0
        ),
        (
            [
                "*.*",
                "...",
                "*.*"
            ],
            4
        )
    ]
)
def test_find_unsafe_gifts(warehouse, expected_count):
    unsafe_gift_count = find_unsafe_gifts(warehouse)

    assert unsafe_gift_count == expected_count
