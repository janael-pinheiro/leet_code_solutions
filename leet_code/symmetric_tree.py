from leet_code.nodes import TreeNode
from typing import Optional


def is_leaf_node(node: Optional[TreeNode]) -> bool:
    return node.left is None and node.right is None


def check_symmetric_nodes(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if (left is None and right is not None) or (left is not None and right is None):
        return False
    elif left is None and right is None:
        return True
    if is_leaf_node(left) and is_leaf_node(right):
        return left.val == right.val
    is_symmetric_left = check_symmetric_nodes(left.left, right.right)
    is_symmetric_right = check_symmetric_nodes(left.right, right.left)
    return is_symmetric_left and is_symmetric_right and (left.val == right.val)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root is None:
        return False
    if is_leaf_node(root):
        return True
    return check_symmetric_nodes(root.left, root.right)
