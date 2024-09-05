from leet_code.number_of_1_bits import hamming_weight
from pytest import mark


@mark.parametrize("n, expected", [
    (11, 3),
    (128, 1),
    (2147483645, 30)
])
def test_hamming_weight(n, expected):
    output = hamming_weight(n)
    assert output == expected
