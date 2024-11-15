from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    container = 0

    while left < right:
        common_height = min(height[left], height[right])
        area = common_height * (right - left)
        if area > container:
            container = area
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return container
