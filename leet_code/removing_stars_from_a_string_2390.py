def remove_stars(s: str) -> str:
    response = ""
    stack = []
    index = 0
    while index < len(s):
        if len(stack) == 0 and s[index] == "*":
            index += 1
            continue
        elif len(stack) > 0 and s[index] == "*":
            stack.pop(0)
            response = response[:-1]
        elif s[index] != "*":
            stack.insert(0, s[index])
            response += s[index]
        index += 1
    return response
