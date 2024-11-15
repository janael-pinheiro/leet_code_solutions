from pytest import mark

from leet_code.container_with_most_water import max_area


@mark.parametrize("height, expected", [
    ([6, 4, 3, 1, 4, 6, 99, 62, 1, 2, 6], 62),
    ([1, 0, 0, 0, 0, 0, 0, 2, 2], 8),
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1, 2], 1)
])
def test_max_area(height, expected):
    output = max_area(height)
    assert expected == output
