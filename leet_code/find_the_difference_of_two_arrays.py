from typing import List


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    distinct_nums1 = set(nums1)
    distinct_nums2 = set(nums2)
    return [list(distinct_nums1 - distinct_nums2), list(distinct_nums2 - distinct_nums1)]
