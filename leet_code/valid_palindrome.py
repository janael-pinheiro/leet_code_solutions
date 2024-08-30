import string


def is_palindrome(s: str) -> bool:
    s = "".join([x.lower() for x in s if x.lower() in string.digits or x.lower() in string.ascii_lowercase])
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
