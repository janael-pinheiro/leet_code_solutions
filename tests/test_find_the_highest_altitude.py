from pytest import mark

from leet_code.find_the_highest_altitude import largest_altitude


@mark.parametrize("gain, expected", [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0)
])
def test_largest_altitude(gain, expected):
    output = largest_altitude(gain)
    assert expected == output
