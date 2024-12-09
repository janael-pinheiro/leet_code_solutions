from typing import List


def _quick_sort(left: int, right: int, nums: List[int]) -> None:
    i = left
    j = right
    pivot = nums[left]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    if left < j:
        _quick_sort(left, j, nums)

    if i < right:
        _quick_sort(i, right, nums)


def sort_colors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    _quick_sort(0, len(nums) - 1, nums)
