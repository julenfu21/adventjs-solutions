import pytest

from solution import is_trees_synchronized


def test_is_trees_synchronized_returns_list():
    tree1 = {"value": "🎄"}
    tree2 = {"value": "🎄"}

    min_steps = is_trees_synchronized(tree1, tree2)

    assert isinstance(min_steps, list)

@pytest.mark.parametrize(
    "tree1,tree2,expected_output",
    [
        pytest.param(
            {"value": "🎄"},
            {"value": "🎄"},
            [True, "🎄"],
            id="test-2"
        ),
        pytest.param(
            {
                "value": "🎄",
                "left": {
                    "value": "⭐"
                },
                "right": {
                    "value": "🎅"
                }
            },
            {
                "value": "🎄",
                "left": {
                    "value": "🎅"
                },
                "right": {
                    "value": "⭐"
                }
            },
            [True, "🎄"],
            id="test-3"
        ),
        pytest.param(
            {
                "value": "✨",
                "left": {
                    "value": "⭐"
                },
                "right": {
                    "value": "🎅"
                }
            },
            {
                "value": "✨",
                "left": {
                    "value": "🎅"
                },
                "right": {
                    "value": "🎁"
                }
            },
            [False, "✨"],
            id="test-4"
        ),
        pytest.param(
            {"value": "🎁"},
            {"value": "🎁"},
            [True, "🎁"],
            id="test-5"
        ),
        pytest.param(
            {"value": "🎄"},
            {"value": "🎁"},
            [False, "🎄"],
            id="test-6"
        ),
        pytest.param(
            {
                "value": "🎄",
                "left": {
                    "value": "⭐"
                }
            },
            {
                "value": "🎄",
                "right": {
                    "value": "⭐"
                }
            },
            [True, "🎄"],
            id="test-7"
        )
    ]
)
def test_is_trees_synchronized(tree1, tree2, expected_output):
    output = is_trees_synchronized(tree1, tree2)

    assert output == expected_output
