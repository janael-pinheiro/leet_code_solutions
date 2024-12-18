from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:
        return [[strs[0]]]
    mapping = {}
    for s in strs:
        sorted_string = "".join(sorted(s))
        hashed_sorted_string = hash(sorted_string)
        anagrams = mapping.get(hashed_sorted_string, [])
        anagrams.append(s)
        mapping[hashed_sorted_string] = anagrams
    return [value for value in mapping.values()]
