from typing import List


def eval_rpn(tokens: List[str]) -> int:
    valid_operators = ["+", "-", "*", "/"]
    stack = []
    for token in tokens:
        if token in valid_operators:
            first_operand = stack.pop(0)
            second_operand = stack.pop(0)
            if token == "+":
                result = first_operand + second_operand
            elif token == "-":
                result = second_operand - first_operand
            elif token == "*":
                result = first_operand * second_operand
            else:
                result = int(second_operand / first_operand)
            stack.insert(0, result)
        else:
            stack.insert(0, int(token))

    return stack.pop(0)
