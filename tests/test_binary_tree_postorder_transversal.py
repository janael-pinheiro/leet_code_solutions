from leet_code.binary_tree_postorder_transversal import post_order_transversal
from pytest import mark


@mark.parametrize("root, expected", [
    ([1, None, 2, 3], [3, 2, 1]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
    ([], [])
])
def test_post_order_transversal(root, expected, build_tree):
    output = post_order_transversal(build_tree(root))
    assert expected == output
