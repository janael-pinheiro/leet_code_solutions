from pytest import mark

from leet_code.can_place_flowers import can_place_flowers


@mark.parametrize("flowerbed, n, expected", [
    ([1, 0, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 1], 2, False),
    ([0, 1, 0, 1, 0, 1, 0, 0], 1, True),
    ([1, 0, 0, 0, 1], 1, True)
])
def test_can_place_flowers(flowerbed, n, expected):
    output = can_place_flowers(flowerbed, n)
    assert expected == output
