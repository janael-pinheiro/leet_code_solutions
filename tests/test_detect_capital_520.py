from pytest import mark

from leet_code.detect_capital_520 import detect_capital_use


@mark.parametrize("word, expected", [
    ("USA", True),
    ("FlaG", False)
])
def test_detect_capital_use(word, expected):
    output = detect_capital_use(word)
    assert expected == output
