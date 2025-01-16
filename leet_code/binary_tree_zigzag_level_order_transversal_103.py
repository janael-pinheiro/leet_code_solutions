from typing import Optional, List

from leet_code.nodes import TreeNode


class Solution:
    def __level_order_transversal(self, root: TreeNode) -> List[List[int]]:
        should_reverse = False
        count = 0
        expected_number_of_nodes = 1
        number_nodes_next_layer = 0
        nodes_per_layer = []
        queue = [root]
        stack = []
        response = []
        while len(queue) > 0:
            current = queue.pop(0)
            count += 1
            if current.left is not None:
                queue.append(current.left)
                number_nodes_next_layer += 1
            if current.right is not None:
                queue.append(current.right)
                number_nodes_next_layer += 1

            if should_reverse:
                stack.insert(0, current.val)
            else:
                nodes_per_layer.append(current.val)

            if count == expected_number_of_nodes:
                if should_reverse:
                    response.append(stack)
                else:
                    response.append(nodes_per_layer)
                count = 0
                nodes_per_layer = []
                stack = []
                expected_number_of_nodes = number_nodes_next_layer
                number_nodes_next_layer = 0
                should_reverse = not should_reverse
        return response

    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]]
        else:
            return self.__level_order_transversal(root)
