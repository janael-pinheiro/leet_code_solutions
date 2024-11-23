def reverse_words(s: str) -> str:
    phrase = " ".join(s.split())
    index = len(phrase) - 1
    result = ""
    while index >= 0:
        stack = []
        while phrase[index] != ' ' and index >= 0:
            stack.insert(0, phrase[index])
            index -= 1
        while len(stack) > 0:
            letter = stack.pop(0)
            result += letter
        if index > 0:
            result += ' '
        index -= 1
    return result
