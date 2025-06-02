# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from leet_code.nodes import ListNode, TreeNode


class Solution:
    def __build_tree(self, values: List[int], left, right):
        if left > right:
            return None
        middle = (left + right) // 2
        root = TreeNode(values[middle])
        left_tree = self.__build_tree(values, left, middle - 1)
        right_tree = self.__build_tree(values, middle + 1, right)
        root.left = left_tree
        root.right = right_tree
        return root

    def sorted_list_to_BST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next
        return self.__build_tree(values, 0, len(values) - 1)
