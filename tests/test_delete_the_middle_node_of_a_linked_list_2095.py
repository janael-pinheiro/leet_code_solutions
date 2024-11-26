from leet_code.delete_the_middle_node_of_a_linked_list_2095 import delete_middle

from pytest import mark


@mark.parametrize("head, expected", [
    ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
    ([1, 2, 3, 4], [1, 2, 4]),
    ([2, 1], [2])
])
def test_delete_middle(head, expected, build_list_nodes):
    output = delete_middle(build_list_nodes(head))
    assert build_list_nodes(expected) == output
