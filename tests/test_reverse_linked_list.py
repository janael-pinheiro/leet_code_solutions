from leet_code.reverse_linked_list import reverse_list
from pytest import mark


@mark.parametrize("head, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([], [])
])
def test_reverse_list(head, expected, build_list_nodes):
    output = reverse_list(build_list_nodes(head))
    assert build_list_nodes(expected) == output
