from typing import Optional

from leet_code.nodes import TreeNode


class Solution:
    def __pre_order_transversal(self, root: TreeNode):
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        left = self.__pre_order_transversal(root.left)
        right = self.__pre_order_transversal(root.right)
        if right is not None:
            right.left = None
        if left is not None:
            current = left
            while current.right is not None:
                current = current.right
            current.right = right
            current.left = None
            root.right = left
            root.left = None
        else:
            root.right = right
        root.left = None
        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.__pre_order_transversal(root)
