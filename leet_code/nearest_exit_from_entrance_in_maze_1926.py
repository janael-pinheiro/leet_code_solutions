from typing import List


def _exit_found(current, entrance, maze):
    is_border = (
            (current[0] == 0 or current[0] == len(maze) - 1) or (current[1] == 0 or current[1] == len(maze[0]) - 1))
    is_empty = (maze[current[0]][current[1]] == ".")
    return current != entrance and is_border and is_empty


def _can_go_up(current, maze, visited):
    return current[0] - 1 >= 0 and visited[current[0] - 1][current[1]] == 0 and maze[current[0] - 1][current[1]] == "."


def _can_go_down(current, maze, visited):
    return current[0] + 1 < len(maze) and visited[current[0] + 1][current[1]] == 0 and maze[current[0] + 1][
        current[1]] == "."


def _can_go_left(current, maze, visited):
    return current[1] - 1 >= 0 and visited[current[0]][current[1] - 1] == 0 and maze[current[0]][current[1] - 1] == "."


def _can_go_right(current, maze, visited):
    return current[1] + 1 < len(maze[0]) and visited[current[0]][current[1] + 1] == 0 and maze[current[0]][
        current[1] + 1] == "."


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
    queue = [entrance]
    visited = [[0 for _ in range(len(row))] for row in maze]
    visited[entrance[0]][entrance[1]] = 1
    distances = [[0 for _ in range(len(row))] for row in maze]
    while len(queue) > 0:
        current = queue.pop(0)
        current_distance = distances[current[0]][current[1]]
        if _exit_found(current, entrance, maze):
            return current_distance
        if _can_go_up(current, maze, visited):
            visited[current[0] - 1][current[1]] = 1
            queue.append([current[0] - 1, current[1]])
            distances[current[0] - 1][current[1]] = current_distance + 1
        if _can_go_down(current, maze, visited):
            visited[current[0] + 1][current[1]] = 1
            queue.append([current[0] + 1, current[1]])
            distances[current[0] + 1][current[1]] = current_distance + 1
        if _can_go_left(current, maze, visited):
            visited[current[0]][current[1] - 1] = 1
            queue.append([current[0], current[1] - 1])
            distances[current[0]][current[1] - 1] = current_distance + 1
        if _can_go_right(current, maze, visited):
            visited[current[0]][current[1] + 1] = 1
            queue.append([current[0], current[1] + 1])
            distances[current[0]][current[1] + 1] = current_distance + 1
        visited.append(current)
    return -1
