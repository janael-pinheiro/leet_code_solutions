from typing import List
from pytest import fixture

from leet_code.maximum_depth_of_binary_tree import TreeNode


@fixture(scope="function")
def build_tree():
    def wrapper(nodes: List[int]) -> TreeNode:
        root = TreeNode(nodes[0])
        queue = [root]
        index = 1
        while index < len(nodes):
            current = queue.pop(0)
            if index < len(nodes):
                current.left = TreeNode(nodes[index])
                queue.append(current.left)
                index += 1
            if index < len(nodes):
                current.right = TreeNode(nodes[index])
                queue.append(current.right)
                index += 1
        return root
    return wrapper
