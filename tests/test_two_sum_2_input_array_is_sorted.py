from leet_code.two_sum_2_input_array_is_sorted import two_sum
from pytest import mark


@mark.parametrize("numbers, target, expected", [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2])
])
def test_two_sum(numbers, target, expected):
    output = two_sum(numbers, target)
    assert output == expected
