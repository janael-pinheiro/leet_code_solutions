from typing import Optional

from leet_code.nodes import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__values = []
        if root.left is None and root.right is None:
            self.__values.append(root.val)
        else:
            self.__inorder_transversal(root)
        self.__size = len(self.__values)
        self.__index = 0

    def __inorder_transversal(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        left_node = self.__inorder_transversal(root.left)
        if left_node is not None:
            self.__values.append(left_node.val)
        self.__values.append(root.val)
        right_node = self.__inorder_transversal(root.right)
        if right_node is not None:
            self.__values.append(right_node.val)

    def next(self) -> int:
        value = self.__values[self.__index]
        self.__index += 1
        return value

    def has_next(self) -> bool:
        return self.__index < self.__size
