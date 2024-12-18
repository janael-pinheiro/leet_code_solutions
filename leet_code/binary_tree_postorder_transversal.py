from leet_code.nodes import TreeNode
from typing import Optional, List


def _transversal(root: TreeNode, output: List[int]) -> None:
    if root is None:
        return
    _transversal(root.left, output)
    _transversal(root.right, output)
    output.append(root.val)


def post_order_transversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    output = []
    _transversal(root, output)
    return output
