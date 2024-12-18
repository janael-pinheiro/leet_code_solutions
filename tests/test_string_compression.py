from pytest import mark

from leet_code.string_compression import compress


@mark.parametrize("chars, expected", [
    (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"]),
    (["a"], ["a"]),
    (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], ["a", "b", "1", "2"])
])
def test_compress(chars, expected):
    compress(chars)
    assert expected == chars
