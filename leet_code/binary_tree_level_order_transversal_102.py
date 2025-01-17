from typing import Optional, List

from leet_code.nodes import TreeNode


class Solution:
    def __level_order_transversal(self, root) -> List[List[int]]:
        response = []
        queue = [root]
        count = 0
        expected_number_of_nodes_layer = 1
        next_layer_number_nodes = 0
        nodes_per_layer = []
        while len(queue) > 0:
            current = queue.pop(0)
            nodes_per_layer.append(current.val)
            count += 1
            if current.left is not None:
                next_layer_number_nodes += 1
                queue.append(current.left)
            if current.right is not None:
                next_layer_number_nodes += 1
                queue.append(current.right)

            if count == expected_number_of_nodes_layer:
                response.append(nodes_per_layer)
                nodes_per_layer = []
                count = 0
                expected_number_of_nodes_layer = next_layer_number_nodes
                next_layer_number_nodes = 0

        return response

    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]]
        else:
            return self.__level_order_transversal(root)
