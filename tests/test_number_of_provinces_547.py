from pytest import mark

from leet_code.number_of_provinces_547 import Solution


@mark.parametrize("is_connected, expected", [
    ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
    ([[1]], 1),
    ([[0]], 0),
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)
])
def test_find_circle_num(is_connected, expected):
    solution = Solution()
    output = solution.find_circle_num(is_connected)
    assert expected == output
