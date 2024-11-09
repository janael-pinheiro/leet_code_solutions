from leet_code.nodes import TreeNode
from typing import Optional, List


def _transversal(root: TreeNode, output: List[int]) -> None:
    if root is None:
        return
    _transversal(root.left, output)
    output.append(root.val)
    _transversal(root.right, output)


def inorder_transversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    output = []
    _transversal(root, output)
    return output

