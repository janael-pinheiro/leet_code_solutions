# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leet_code.nodes import TreeNode


class Solution:
    def __level_order_transversal(self, root):
        expected_number_nodes = 1
        next_level_number_nodes = 0
        count_nodes = 0
        queue = [root]
        left_nodes = []
        next_left_nodes = []
        while len(queue) > 0:
            current = queue.pop(0)
            count_nodes += 1
            if current.left is not None:
                next_level_number_nodes += 1
                queue.append(current.left)
                next_left_nodes.append(current.left)
            if current.right is not None:
                next_level_number_nodes += 1
                queue.append(current.right)
                if len(next_left_nodes) == 0:
                    next_left_nodes.append(current.right)
            if count_nodes == expected_number_nodes:
                count_nodes = 0
                expected_number_nodes = next_level_number_nodes
                next_level_number_nodes = 0
                if len(queue) == 0:
                    return left_nodes[0].val
                else:
                    left_nodes = next_left_nodes
                    next_left_nodes = []

    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val
        return self.__level_order_transversal(root)
