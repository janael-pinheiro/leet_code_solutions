from typing import List, Union
from pytest import fixture

from leet_code.tree_node import TreeNode


@fixture(scope="function")
def build_tree():
    def wrapper(nodes: List[int]) -> Union[TreeNode, None]:
        if len(nodes) == 0:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        index = 1
        while index < len(nodes):
            current = queue.pop(0)
            if current is None:
                continue
            if index < len(nodes):
                if nodes[index] is None:
                    current.left = None
                else:
                    current.left = TreeNode(nodes[index])
                queue.append(current.left)
                index += 1
            if index < len(nodes):
                if nodes[index] is None:
                    current.right = None
                else:
                    current.right = TreeNode(nodes[index])
                queue.append(current.right)
                index += 1
        return root
    return wrapper
