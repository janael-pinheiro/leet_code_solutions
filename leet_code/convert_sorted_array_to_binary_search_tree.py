# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from leet_code.nodes import TreeNode


class Solution:
    def __divide_and_conquer(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        middle = (left + right) // 2
        root = TreeNode(nums[middle])
        left_tree = self.__divide_and_conquer(nums, left, middle - 1)
        right_tree = self.__divide_and_conquer(nums, middle + 1, right)
        root.left = left_tree
        root.right = right_tree
        return root

    def sorted_array_to_BST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.__divide_and_conquer(nums, 0, len(nums)-1)
