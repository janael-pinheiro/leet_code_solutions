def _gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return _gcd(b, a % b)


def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:_gcd(len(str1), len(str2))]
