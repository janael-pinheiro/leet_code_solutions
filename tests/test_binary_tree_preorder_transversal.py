from leet_code.binary_tree_preorder_transversal import preorder_transversal
from pytest import mark


@mark.parametrize("root, expected", [
    ([1, None, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9])
])
def test_preorder_transversal(root, expected, build_tree):
    output = preorder_transversal(build_tree(root))
    assert expected == output
