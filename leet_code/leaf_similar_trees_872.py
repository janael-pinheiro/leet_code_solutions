from typing import Optional, List

from leet_code.nodes import TreeNode


def _get_leaves(root: Optional[TreeNode], output: List[int]) -> List[int]:
    if root is None:
        return output
    if root.left is None and root.right is None:
        output.append(root.val)
        return output

    left_output = _get_leaves(root.left, output)
    right_output = _get_leaves(root.right, left_output)
    return right_output


def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    root1_leaves = _get_leaves(root1, [])
    root2_leaves = _get_leaves(root2, [])
    index = 0
    if len(root1_leaves) != len(root2_leaves):
        return False
    while index < len(root1_leaves) and index < len(root2_leaves):
        if root1_leaves[index] != root2_leaves[index]:
            return False
        index += 1
    return True
