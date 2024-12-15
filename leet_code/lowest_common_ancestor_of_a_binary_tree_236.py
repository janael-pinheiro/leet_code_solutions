from typing import Tuple

from leet_code.nodes import TreeNode


def _post_order_transversal(root, p, q) -> Tuple[TreeNode | None, bool]:
    if root is None:
        return None, False
    elif root.left is None and root.right is None:
        if root.val == p.val or root.val == q.val:
            return root, False
        return None, False
    left_node, left_found = _post_order_transversal(root.left, p, q)
    right_node, right_found = _post_order_transversal(root.right, p, q)
    if left_node and right_node:
        return root, True
    elif root.val == p.val or root.val == q.val:
        if left_node or right_node:
            return root, True
        return root, True
    elif left_found:
        return left_node, True
    elif left_node:
        return left_node, False
    elif right_found:
        return right_node, True
    elif right_node:
        return right_node, False
    return None, False


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    return _post_order_transversal(root, p, q)[0]
