from pytest import mark

from leet_code.min_stack_155 import MinStack


@mark.parametrize("operation, input_data, expected", [
    (
        ["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top", "getMin", "push", "top", "getMin", "pop", "getMin"],
        [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648], [], [], [], []],
        [None,None,None,None,2147483647,None,2147483646,None,2147483646,None,None,2147483647,2147483647,None,-2147483648,-2147483648,None,2147483647]
    ),
    (
        ["MinStack","push","push","push","getMin","pop","top","getMin"],
        [[],[-2],[0],[-3],[],[],[],[]],
        [None,None,None,None,-3,None,0,-2]
    )
])
def test_min_stack(operation, input_data, expected):
    min_stack = MinStack()
    output = [None]
    for op, input_value in zip(operation, input_data):
        if op == "push":
            min_stack.push(input_value[0])
            output.append(None)
        elif op == "getMin":
            output.append(min_stack.getMin())
        elif op == "top":
            output.append(min_stack.top())
        elif op == "pop":
            output.append(min_stack.pop())
    assert output == expected
