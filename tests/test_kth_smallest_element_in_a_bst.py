from leet_code.kth_smallest_element_in_a_bst import kth_smallest
from pytest import mark


@mark.parametrize("head, k, expected", [
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3)
])
def test_kth_smallest(head, k, expected, build_tree):
    output = kth_smallest(build_tree(head), k)
    assert output == expected
