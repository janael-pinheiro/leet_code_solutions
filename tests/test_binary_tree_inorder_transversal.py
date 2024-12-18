from leet_code.binary_tree_inorder_transversal import inorder_transversal
from pytest import mark


@mark.parametrize("root, expected", [
    ([1, None, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8])
])
def test_inorder_transversal(root, expected, build_tree):
    root_tree = build_tree(root)
    output = inorder_transversal(root_tree)
    assert expected == output
