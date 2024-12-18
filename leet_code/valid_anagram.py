from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_counter = Counter(s)
    t_counter = Counter(t)
    for key, value in t_counter.items():
        if key not in s_counter:
            return False
        elif key in s_counter and value > s_counter.get(key):
            return False
    return True
