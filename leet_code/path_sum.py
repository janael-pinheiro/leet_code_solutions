from leet_code.maximum_depth_of_binary_tree import TreeNode
from typing import Optional


def has_path(root: Optional[TreeNode], targetSum: int, current_sum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return targetSum == current_sum + root.val
    has_sum_left = has_path(root.left, targetSum, current_sum + root.val)
    if has_sum_left:
        return True
    has_sum_right = has_path(root.right, targetSum, current_sum + root.val)
    if has_sum_right:
        return True
    return False


def has_path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    elif root.left is None and root.right is None and root.val == targetSum:
        return True
    has_sum_left = has_path(root.left, targetSum, root.val)
    if has_sum_left:
        return has_sum_left
    has_sum_right = has_path(root.right, targetSum, root.val)
    if has_sum_right:
        return has_sum_right
    return False
