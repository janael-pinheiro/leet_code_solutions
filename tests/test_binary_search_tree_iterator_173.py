from pytest import mark

from leet_code.binary_search_tree_iterator_173 import BSTIterator


@mark.parametrize("operation, input_data, expected", [
    (["BSTIterator", "hasNext", "next", "hasNext"], [[[1]], [], [], []], [None, True, 1, False]),
    (["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"], [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []], [None, 3, 7, True, 9, True, 15, True, 20, False])
])
def test_binary_search_tree_iterator(operation, input_data, expected, build_tree):
    iterator = None
    output = []
    for op, input_value in zip(operation, input_data):
        if op == "BSTIterator":
            iterator = BSTIterator(build_tree(input_value[0]))
            output.append(None)
        elif op == "next":
            output.append(iterator.next())
        elif op == "hasNext":
            output.append(iterator.has_next())
    assert output == expected
