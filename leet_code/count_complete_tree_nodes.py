from leet_code.nodes import TreeNode
from typing import Optional


def is_leaf_node(node: Optional[TreeNode]) -> bool:
    return node.right is None and node.left is None


def count_nodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if is_leaf_node(root):
        return 1
    number_nodes = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current is None:
            continue
        queue.append(current.right)
        queue.append(current.left)
        number_nodes += 1

    return number_nodes
