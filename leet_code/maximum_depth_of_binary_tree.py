from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None


def max_depth(root: Optional[TreeNode]):
    if root is None:
        return 0
    max_left = max_depth(root.left)
    max_right = max_depth(root.right)
    current_max = max(max_left, max_right)
    return current_max + 1
