# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from leet_code.nodes import TreeNode


class Solution:
    def __build_tree(self, children, key):
        if key not in children:
            return TreeNode(key)
        root = children[key]
        if root.left is not None:
            left_tree = self.__build_tree(children, root.left.val)
            root.left = left_tree
        if root.right is not None:
            right_tree = self.__build_tree(children, root.right.val)
            root.right = right_tree
        return root

    def create_binary_tree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        values = []
        child_parent_mapping = {}
        children = {}
        for description in descriptions:
            child_parent_mapping[description[1]] = description[0]
            c = children.get(description[0], TreeNode(description[0]))
            current = TreeNode(description[1])
            if description[2] == 1:
                c.left = current
            else:
                c.right = current
            children[description[0]] = c
        root = None
        for child in children.keys():
            if child not in child_parent_mapping:
                root = child
                break
        return self.__build_tree(children, root)
