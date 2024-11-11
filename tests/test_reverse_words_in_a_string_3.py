from leet_code.reverse_words_in_a_string_3 import reverse_words
from pytest import mark


@mark.parametrize("s, expected", [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("Mr Ding", "rM gniD")
])
def test_reverse_words(s, expected):
    output = reverse_words(s)
    assert expected == output
