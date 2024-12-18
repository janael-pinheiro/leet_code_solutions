from leet_code.nodes import TreeNode


def _depth_first_search(root: TreeNode, max_value: int) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if root.val >= max_value:
            return 1
        return 0
    left_count = _depth_first_search(root.left, max(max_value, root.val))
    right_count = _depth_first_search(root.right, max(max_value, root.val))
    children_count = left_count + right_count
    if root.val >= max_value:
        return children_count + 1
    return children_count


def good_nodes(root: TreeNode) -> int:
    if root.right is None and root.left is None:
        return 1
    return _depth_first_search(root, max(root.val, -10 ** 5))
