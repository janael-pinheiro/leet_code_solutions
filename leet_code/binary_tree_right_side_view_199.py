from typing import Optional, List

from leet_code.nodes import TreeNode


def _breadth_first_search(root: TreeNode) -> List[int]:
    queue = [root]
    stack = []
    response = []
    count = 0
    count_nodes = 0
    expected_number_nodes_per_layer = 1
    while len(queue) > 0:
        current = queue.pop(0)
        if current is not None:
            count_nodes += 1
            stack.insert(0, current)
        count += 1
        if count == expected_number_nodes_per_layer:
            count = 0
            expected_number_nodes_per_layer = 2 * count_nodes
            count_nodes = 0
            if len(stack) > 0:
                top = stack.pop(0)
                response.append(top.val)
                stack = []
        if current is None:
            continue
        queue.append(current.left)
        queue.append(current.right)
    if len(stack) > 0:
        response.append(stack.pop(0).val)
    return response


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return _breadth_first_search(root)
