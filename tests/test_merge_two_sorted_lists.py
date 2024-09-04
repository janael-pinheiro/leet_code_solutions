from leet_code.merge_two_sorted_lists import merge_two_lists
from pytest import mark


@mark.parametrize("list1, list2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    ([5], [1, 2, 4], [1, 2, 4, 5]),
    ([-9, -7, -3, -3, -1, 2, 3], [-7, -7, -6, -6, -5, -3, 2, 4], [-9, -7, -7, -7, -6, -6, -5, -3, -3, -3, -1, 2, 2, 3, 4])
])
def test_merge_two_lists(list1, list2, expected, build_list_nodes):
    list1_head = build_list_nodes(list1)
    list2_head = build_list_nodes(list2)
    expected_head = build_list_nodes(expected)
    output = merge_two_lists(list1_head, list2_head)
    assert output == expected_head
