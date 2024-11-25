from typing import Optional

from leet_code.nodes import TreeNode


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return root
    if root.val == val:
        return root
    elif root.val < val:
        return search_bst(root.right, val)
    else:
        return search_bst(root.left, val)
