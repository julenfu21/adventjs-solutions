from typing import Literal


def is_trees_synchronized(tree1, tree2):

    def get_subtree_or_none(tree: dict, side: Literal["left", "right"]) -> dict | None:
        if side in tree:
            return tree[side]

        return None

    def are_trees_equal(tree1: dict | None, tree2: dict | None) -> bool:
        if not (tree1 and tree2):
            return True

        if any(
            [not tree1 and tree2, tree1 and not tree2, tree1["value"] != tree2["value"]]
        ):
            return False

        return are_trees_equal(
            tree1=get_subtree_or_none(tree1, "left"),
            tree2=get_subtree_or_none(tree2, "right"),
        ) and are_trees_equal(
            tree1=get_subtree_or_none(tree1, "right"),
            tree2=get_subtree_or_none(tree2, "left"),
        )

    # Code here
    return [are_trees_equal(tree1, tree2), tree1["value"]]
