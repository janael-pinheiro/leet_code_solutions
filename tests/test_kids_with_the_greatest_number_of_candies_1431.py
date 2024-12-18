from leet_code.kids_with_the_greatest_number_of_candies_1431 import kids_with_candies

from pytest import mark


@mark.parametrize("candies, extra_candies, expected", [
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True])
])
def test_kids_with_candies(candies, extra_candies, expected):
    output = kids_with_candies(candies, extra_candies)
    assert expected == output
