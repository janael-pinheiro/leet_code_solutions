from typing import List


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    visited_rooms = set()
    stack = [[0]]
    while len(stack) > 0:
        current = stack.pop(0)
        for curr in current:
            if curr not in visited_rooms:
                visited_rooms.add(curr)
                stack.insert(0, rooms[curr])

    return len(visited_rooms) == len(rooms)
