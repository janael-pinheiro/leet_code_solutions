from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True

    if len(flowerbed) == 1:
        if n == 1 and flowerbed[0] == 0:
            return True
        return False

    index = 0
    while index < len(flowerbed) and n > 0:
        if index == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
            n -= 1
            flowerbed[index] = 1
        elif index == len(flowerbed) - 1 and flowerbed[index] == 0 and flowerbed[index - 1] == 0:
            n -= 1
            flowerbed[index] = 1
        elif flowerbed[index] == 0 and flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
            n -= 1
            flowerbed[index] = 1
        index += 1

    return n == 0
