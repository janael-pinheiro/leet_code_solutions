from leet_code.flatten_binary_tree_to_linked_list_114 import Solution

from pytest import mark


@mark.parametrize("root, expected", [
    ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
    ([], []),
    ([0], [0])
])
def test_flatten(root, expected, build_tree):
    solution = Solution()
    tree_root = build_tree(root)
    solution.flatten(tree_root)
    assert tree_root == build_tree(expected)
