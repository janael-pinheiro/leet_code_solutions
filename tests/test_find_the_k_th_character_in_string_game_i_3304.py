from leet_code.find_the_k_th_character_in_string_game_I_3304 import kth_character
from pytest import mark


@mark.parametrize("k, expected", [
    (5, "b"),
    (10, "c")
])
def test_kth_character(k, expected):
    output = kth_character(k)
    assert expected == output
