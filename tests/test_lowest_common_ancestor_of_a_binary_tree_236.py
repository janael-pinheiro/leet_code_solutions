from pytest import mark

from leet_code.lowest_common_ancestor_of_a_binary_tree_236 import lowest_common_ancestor


@mark.parametrize("root, p, q, expected", [
    ([1, 2], [1], [2], 1),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [5], [4], 5),
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [5], [1], 3),
    ([1, 2, 3, None, 4], [4], [3], 1)
])
def test_lowest_common_ancestor(root, p, q, expected, build_tree):
    output = lowest_common_ancestor(build_tree(root), build_tree(p), build_tree(q))
    assert expected == output.val
