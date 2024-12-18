from typing import List


def _binary_search(nums: List[int], target: int) -> int:
    if target > nums[-1]:
        return -1
    elif target <= nums[0]:
        return 0
    left = 0
    right = len(nums) - 1
    middle = (left + right) // 2
    while left <= right:
        if target > nums[middle]:
            left = middle + 1
        elif target <= nums[middle]:
            right = middle - 1
        middle = (left + right) // 2
    while middle < len(nums) and target > nums[middle]:
        middle += 1
    return middle


def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    sorted_potions = sorted(potions)
    response = []
    for spell in spells:
        target = success // spell
        if success % spell != 0:
            target += 1
        index = _binary_search(sorted_potions, target)
        if index == -1:
            response.append(0)
        else:
            response.append(len(sorted_potions) - index)
    return response
