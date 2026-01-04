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
        pytest.param(
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
            ).rstrip(),
            id="test-2"
        ),
        pytest.param(
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
            ).rstrip(),
            id="test-3"
        ),
        pytest.param(
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
            ).rstrip(),
            id="test-4"
        ),
        pytest.param(
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
            ).rstrip(),
            id="test-5"
        ),
        pytest.param(
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
            ).rstrip(),
            id="test-6"
        ),
        pytest.param(
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
            ).rstrip(),
            id="test-7"
        )
    ]
)
def test_draw_table(data, sort_by, expected_table):
    table = draw_table(data, sort_by)

    assert table == expected_table
