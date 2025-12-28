from textwrap import dedent

import pytest

from solution import draw_table


def test_draw_table_returns_string():
    data = [
        { "name": "Alice", "city": "London" }
    ]
    sort_by = "name"

    table = draw_table(data, sort_by)

    assert isinstance(table, str)

@pytest.mark.parametrize(
    "data,sort_by,expected_table",
    [
        (
            [
                { "name": "Charlie", "city": "New York" },
                { "name": "Alice", "city": "London" },
                { "name": "Bob", "city": "Paris" }
            ],
            "name",
            dedent(
                """\
                +---------+----------+
                | A       | B        |
                +---------+----------+
                | Alice   | London   |
                | Bob     | Paris    |
                | Charlie | New York |
                +---------+----------+
                """
            ).rstrip()
        ),
        (
            [
                { "gift": "Book", "quantity": 5 },
                { "gift": "Music CD", "quantity": 1 },
                { "gift": "Doll", "quantity": 10 }
            ],
            "quantity",
            dedent(
                """\
                +----------+----+
                | A        | B  |
                +----------+----+
                | Music CD | 1  |
                | Book     | 5  |
                | Doll     | 10 |
                +----------+----+
                """
            ).rstrip()
        ),
        (
            [
                { "name": "Alice", "city": "Paris" },
                { "name": "Bob", "city": "London" }
            ],
            "city",
            dedent(
                """\
                +-------+--------+
                | A     | B      |
                +-------+--------+
                | Bob   | London |
                | Alice | Paris  |
                +-------+--------+
                """
            ).rstrip()
        ),
        (
            [
                { "name": "Alice", "city": "London" }
            ],
            "name",
            dedent(
                """\
                +-------+--------+
                | A     | B      |
                +-------+--------+
                | Alice | London |
                +-------+--------+
                """
            ).rstrip()
        ),
        (
            [
                { "a": 2, "b": "Y", "c": "X" },
                { "a": 1, "b": "Z", "c": "W" },
                { "a": 3, "b": "A", "c": "B" }
            ],
            "a",
            dedent(
                """\
                +---+---+---+
                | A | B | C |
                +---+---+---+
                | 1 | Z | W |
                | 2 | Y | X |
                | 3 | A | B |
                +---+---+---+
                """
            ).rstrip()
        ),
        (
            [
                { "id": "zebra", "active": True },
                { "id": "alpha", "active": False }
            ],
            "id",
            dedent(
                """\
                +-------+-------+
                | A     | B     |
                +-------+-------+
                | alpha | False |
                | zebra | True  |
                +-------+-------+
                """
            ).rstrip()
        )
    ]
)
def test_find_gift_path(data, sort_by, expected_table):
    table = draw_table(data, sort_by)

    assert table == expected_table
