import pytest

from solution import match_gloves


def test_match_gloves_returns_list():
    gloves = []

    matched_gloves = match_gloves(gloves)

    assert isinstance(matched_gloves, list)

@pytest.mark.parametrize(
    "gloves,expected_matches", [
        (
            [
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'L', "color": "green"}
            ],
            ["red", "green"]
        ),
        (
            [
                {"hand": 'L', "color": "gold"},
                {"hand": 'R', "color": "gold"},
                {"hand": 'L', "color": "gold"},
                {"hand": 'L', "color": "gold"},
                {"hand": 'R', "color": "gold"}
            ],
            ["gold", "gold"]
        ),
        (
            [
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "blue"}
            ],
            []
        ),
        (
            [
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'R', "color": "green"}
            ],
            ["red", "green"]
        ),
        (
            [
                {"hand": 'R', "color": "blue"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'R', "color": "blue"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'L', "color": "blue"}
            ],
            ["blue", "blue"]
        ),
        (
            [
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"}
            ],
            ["red", "green"]
        ),
        (
            [
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'L', "color": "red"},
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"}
            ],
            []
        ),
        (
            [
                {"hand": 'L', "color": "silver"},
                {"hand": 'L', "color": "silver"},
                {"hand": 'R', "color": "silver"},
                {"hand": 'R', "color": "silver"},
                {"hand": 'R', "color": "silver"}
            ],
            ["silver", "silver"]
        )
    ]
)
def test_match_gloves(gloves, expected_matches):
    matched_gloves = match_gloves(gloves)

    assert matched_gloves == expected_matches
