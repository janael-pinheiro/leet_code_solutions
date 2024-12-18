from leet_code.remove_duplicates_from_sorted_list import delete_duplicates
from pytest import mark


@mark.parametrize("head, expected", [
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([1, 1, 1], [1])
])
def test_remove_duplicates(head, expected, build_list_nodes):
    output = delete_duplicates(build_list_nodes(head))
    assert build_list_nodes(expected) == output
