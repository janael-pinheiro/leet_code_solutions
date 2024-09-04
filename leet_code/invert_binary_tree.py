from leet_code.nodes import TreeNode
from typing import Optional


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    if root.left is None and root.right is None:
        return root
    right = invert_tree(root.right)
    left = invert_tree(root.left)
    root.left = right
    root.right = left
    return root


