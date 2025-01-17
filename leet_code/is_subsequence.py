def is_subsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        return True
    return False
