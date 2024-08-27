from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    length_ransom_note = len(ransomNote)
    length_magazine = len(magazine)
    if length_ransom_note > length_magazine:
        return False
    ransom_note_counter = Counter(ransomNote)
    magazine_counter = Counter(magazine)
    response = True
    for key, value in ransom_note_counter.items():
        if key not in magazine_counter or (key in magazine_counter and value > magazine_counter[key]):
            response = False
            break
    return response
