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
        (
            {"value": "🎄"},
            {"value": "🎄"},
            [True, "🎄"]
        ),
        (
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
            [True, "🎄"]
        ),
        (
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
            [False, "✨"]
        ),
        (
            {"value": "🎁"},
            {"value": "🎁"},
            [True, "🎁"]
        ),
        (
            {"value": "🎄"},
            {"value": "🎁"},
            [False, "🎄"]
        ),
        (
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
            [True, "🎄"]
        )
    ]
)
def test_is_trees_synchronized(tree1, tree2, expected_output):
    output = is_trees_synchronized(tree1, tree2)

    assert output == expected_output
