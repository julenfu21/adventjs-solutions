import pytest

from solution import match_gloves


def test_match_gloves_returns_list():
    gloves = []

    matched_gloves = match_gloves(gloves)

    assert isinstance(matched_gloves, list)

@pytest.mark.parametrize(
    "gloves,expected_matches", [
        pytest.param(
            [
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'L', "color": "green"}
            ],
            ["red", "green"],
            id="test-2"
        ),
        pytest.param(
            [
                {"hand": 'L', "color": "gold"},
                {"hand": 'R', "color": "gold"},
                {"hand": 'L', "color": "gold"},
                {"hand": 'L', "color": "gold"},
                {"hand": 'R', "color": "gold"}
            ],
            ["gold", "gold"],
            id="test-3"
        ),
        pytest.param(
            [
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "blue"}
            ],
            [],
            id="test-4"
        ),
        pytest.param(
            [
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'R', "color": "green"}
            ],
            ["red", "green"],
            id="test-5"
        ),
        pytest.param(
            [
                {"hand": 'R', "color": "blue"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'R', "color": "blue"},
                {"hand": 'L', "color": "blue"},
                {"hand": 'L', "color": "blue"}
            ],
            ["blue", "blue"],
            id="test-6"
        ),
        pytest.param(
            [
                {"hand": 'R', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'R', "color": "red"},
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"}
            ],
            ["red", "green"],
            id="test-7"
        ),
        pytest.param(
            [
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"},
                {"hand": 'L', "color": "red"},
                {"hand": 'L', "color": "green"},
                {"hand": 'L', "color": "red"}
            ],
            [],
            id="test-8"
        ),
        pytest.param(
            [
                {"hand": 'L', "color": "silver"},
                {"hand": 'L', "color": "silver"},
                {"hand": 'R', "color": "silver"},
                {"hand": 'R', "color": "silver"},
                {"hand": 'R', "color": "silver"}
            ],
            ["silver", "silver"],
            id="test-9"
        )
    ]
)
def test_match_gloves(gloves, expected_matches):
    matched_gloves = match_gloves(gloves)

    assert matched_gloves == expected_matches
