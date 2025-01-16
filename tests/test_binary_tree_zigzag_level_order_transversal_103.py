from leet_code.binary_tree_zigzag_level_order_transversal_103 import Solution

from pytest import mark


@mark.parametrize("root, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
    ([1], [[1]]),
    ([], [])
])
def test_binary_tree_zigzag_level_order_transversal(root, expected, build_tree):
    solution = Solution()
    output = solution.zigzag_level_order(build_tree(root))
    assert output == expected
