from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    stack = [asteroids[0]]
    index = 1
    while index < len(asteroids):
        if len(stack) == 0:
            stack.insert(0, asteroids[index])
            index += 1
            continue

        current = stack.pop(0)
        has_collision = False
        while current > 0 > asteroids[index]:
            has_collision = True
            if len(stack) > 0 and abs(current) < abs(asteroids[index]):
                current = stack.pop(0)
            elif len(stack) == 0 and abs(current) < abs(asteroids[index]):
                stack.insert(0, asteroids[index])
                break
            elif abs(current) > abs(asteroids[index]):
                stack.insert(0, current)
                break
            else:
                break
            has_collision = False
        if not has_collision:
            stack.insert(0, current)
            stack.insert(0, asteroids[index])

        index += 1

    stack.reverse()
    return stack
