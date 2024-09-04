from typing import List, Union
from pytest import fixture

from leet_code.nodes import TreeNode, ListNode


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


@fixture(scope="function")
def build_list_nodes():
    def wrapper(nodes: List[int]) -> Union[ListNode, None]:
        if len(nodes) == 0:
            return None
        if len(nodes) == 1:
            return ListNode(nodes[0])
        last = ListNode(nodes[-1])
        index = len(nodes) - 2
        while index > 0:
            current = ListNode(nodes[index])
            current.next = last
            last = current
            index -= 1
        head = ListNode(nodes[0])
        head.next = last
        return head
    return wrapper
