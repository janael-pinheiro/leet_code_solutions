from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None


@dataclass
class ListNode:
    val: int
    next: ListNode = None
