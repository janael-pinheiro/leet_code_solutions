from pytest import mark

from leet_code.equal_row_and_column_pairs_2352 import equal_pairs


@mark.parametrize("grid, expected", [
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3)
])
def test_equal_pairs(grid, expected):
    output = equal_pairs(grid)
    assert output == expected
