from leet_code.reverse_linked_list_2 import reverse_between
from pytest import mark


@mark.parametrize("head, left, right, expected", [
    ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
    ([5], 1, 1, [5])
])
def test_reverse_between(head, left, right, expected, build_list_nodes):
    output = reverse_between(build_list_nodes(head), left, right)
    assert output == build_list_nodes(expected)
