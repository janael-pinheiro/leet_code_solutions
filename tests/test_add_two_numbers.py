from leet_code.add_two_numbers import add_two_numbers
from pytest import mark


@mark.parametrize("l1, l2, expected", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
])
def test_add_two_numbers(l1, l2, expected, build_list_nodes):
    output = add_two_numbers(build_list_nodes(l1), build_list_nodes(l2))
    assert output == build_list_nodes(expected)
