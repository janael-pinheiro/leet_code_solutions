from pytest import mark

from leet_code.evaluate_reverse_polish_notation_150 import eval_rpn


@mark.parametrize("tokens, expected", [
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6)
])
def test_eval_rpn(tokens, expected):
    output = eval_rpn(tokens)
    assert expected == output
