from leet_code.search_in_a_binary_search_tree_700 import search_bst

from pytest import mark


@mark.parametrize("root, val, expected", [
    ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
    ([4, 2, 7, 1, 3], 5, [])
])
def test_search_bst(root, val, expected, build_tree):
    output = search_bst(build_tree(root), val)
    assert output == build_tree(expected)
