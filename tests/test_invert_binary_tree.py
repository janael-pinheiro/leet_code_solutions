from leet_code.invert_binary_tree import invert_tree
from pytest import mark


@mark.parametrize("root, expected", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], [])
])
def test_invert_tree(root, expected, build_tree):
    root_tree = build_tree(root)
    expected_tree = build_tree(expected)
    inverted_tree = invert_tree(expected_tree)
    assert root_tree == inverted_tree
