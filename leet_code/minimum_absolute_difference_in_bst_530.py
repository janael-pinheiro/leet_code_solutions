from typing import Optional

from leet_code.nodes import TreeNode


class Solution:
    def transversal(self, root):
        if root is None:
            return 10 ** 5
        if root.left is None and root.right is None:
            return 10 ** 5
        left_tree = self.transversal(root.left)
        right_tree = self.transversal(root.right)
        if root.left is not None:
            left_value = root.left.val
        else:
            left_value = 10 ** 5
        if root.right is not None:
            right_value = root.right.val
        else:
            right_value = 10 ** 5
        left_difference = min(left_tree, abs(root.val - left_value))
        right_difference = min(right_tree, abs(root.val - right_value))
        minimum_difference = min(left_difference, right_difference)
        return minimum_difference

    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        return self.transversal(root)
