# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leet_code.nodes import TreeNode


class Solution:
    def __build_tree(self, nums, left, right):
        if left > right:
            return None
        middle = (left + right) // 2
        root = TreeNode(nums[middle])
        left_subtree = self.__build_tree(nums, left, middle - 1)
        right_subtree = self.__build_tree(nums, middle + 1, right)
        root.left = left_subtree
        root.right = right_subtree
        return root

    def __in_order_transversal(self, root, output):
        if root is None:
            return None
        left_node = self.__in_order_transversal(root.left, output)
        if left_node is not None:
            output.append(left_node.val)
        output.append(root.val)
        right_node = self.__in_order_transversal(root.right, output)
        if right_node is not None:
            output.append(right_node.val)

    def balance_BST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        output = []
        self.__in_order_transversal(root, output)
        return self.__build_tree(output, 0, len(output) - 1)
