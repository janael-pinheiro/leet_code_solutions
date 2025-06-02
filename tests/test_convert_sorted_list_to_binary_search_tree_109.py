from leet_code.convert_sorted_list_to_binary_search_tree_109 import Solution

from pytest import mark


@mark.parametrize("root, expected", [
    ([-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]),
    ([], [])
])
def test_sorted_list_to_BST(root, expected, build_list_nodes, build_tree):
    solution = Solution()
    output = solution.sorted_list_to_BST(build_list_nodes(root))
    assert output == build_tree(expected)
