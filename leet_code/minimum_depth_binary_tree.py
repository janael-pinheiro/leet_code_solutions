from typing import Optional

from leet_code.nodes import TreeNode


def _depth_first_search(root: TreeNode) -> int:
    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        result = _depth_first_search(root.right) + 1
    elif root.right is None:
        result = _depth_first_search(root.left) + 1
    else:
        left_depth = _depth_first_search(root.left)
        right_depth = _depth_first_search(root.right)
        result = min(left_depth, right_depth) + 1
    return result


def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return _depth_first_search(root)
