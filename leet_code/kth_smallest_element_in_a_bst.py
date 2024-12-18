from typing import Optional

from leet_code.nodes import TreeNode


def inorder_traversal(root, k, count=0):
    if root is None:
        return count, -1
    if root.left is None and root.right is None:
        if count + 1 == k:
            return count + 1, root.val
        else:
            return count + 1, -1
    count, value = inorder_traversal(root.left, k, count)
    if value != -1:
        return count + 1, value
    if count + 1 == k:
        return count + 1, root.val
    return inorder_traversal(root.right, k, count + 1)


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    count, value = inorder_traversal(root, k, 0)
    return value
