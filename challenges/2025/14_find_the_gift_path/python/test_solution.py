import pytest

from solution import find_gift_path


def test_find_gift_path_returns_list():
    workshop = {
        "storage": {
            "shelf": {
                "box1": "train",
                "box2": "switch"
            },
            "box": "car"
        },
        "gift": "doll"
    }
    gift = "train"

    gift_path = find_gift_path(workshop, gift)

    assert isinstance(gift_path, list)

@pytest.mark.parametrize(
    "workshop,gift,expected_path",
    [
        pytest.param(
            {
                "storage": {
                    "shelf": {
                        "box1": "train",
                        "box2": "switch"
                    },
                    "box": "car"
                },
                "gift": "doll"
            },
            "train",
            ["storage", "shelf", "box1"],
            id="test-2"
        ),
        pytest.param(
            {
                "storage": {
                    "shelf": {
                        "box1": "train",
                        "box2": "switch"
                    },
                    "box": "car"
                },
                "gift": "doll"
            },
            "switch",
            ["storage", "shelf", "box2"],
            id="test-3"
        ),
        pytest.param(
            {"storage":{"shelf":{"box1":"train","box2":"switch"},"box":"car"},"gift":"doll"},
            "car",
            ["storage", "box"],
            id="test-4"
        ),
        pytest.param(
            {"storage":{"shelf":{"box1":"train","box2":"switch"},"box":"car"},"gift":"doll"},
            "doll",
            ["gift"],
            id="test-5"
        ),
        pytest.param(
            {"storage":{"shelf":{"box1":"train","box2":"switch"},"box":"car"},"gift":"doll"},
            "plane",
            [],
            id="test-6"
        ),
        pytest.param(
            {
                "a": {
                    "b": {
                        "c": 42
                    }
                }
            },
            42,
            ["a", "b", "c"],
            id="test-7"
        ),
        pytest.param(
            {
                "ok": True,
                "nested": {
                    "nope": False,
                    "extra": {
                        "is": 0
                    }
                }
            },
            False,
            ["nested", "nope"],
            id="test-8"
        )
    ]
)
def test_find_gift_path(workshop, gift, expected_path):
    gift_path = find_gift_path(workshop, gift)

    assert gift_path == expected_path
