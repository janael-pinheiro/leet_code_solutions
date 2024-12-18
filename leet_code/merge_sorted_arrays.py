from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            nums1.pop()
            i += 1
            j += 1
            m += 1
        else:
            nums1.insert(i, nums2[j])
            nums1.pop()
            i += 2
            j += 1
            m += 1

    while j < n:
        nums1[i] = nums2[j]
        i += 1
        j += 1
