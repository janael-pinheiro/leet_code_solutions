from typing import List, Optional, Tuple


class Solution:

    def __find_rotten_oranges(self, grid: List[List[int]]) -> Optional[List[List[int]]]:
        queue = []
        row = 0
        while row < len(grid):
            column = 0
            while column < len(grid[row]):
                if grid[row][column] == 2:
                    queue.append([row, column])
                column += 1
            row += 1
        if len(queue) > 0:
            return queue
        return None

    def __count_fresh_oranges(self, grid: List[List[int]]) -> Tuple[int, int]:
        count_fresh = 0
        count_empty = 0
        row = 0
        while row < len(grid):
            column = 0
            while column < len(grid[row]):
                if grid[row][column] == 1:
                    count_fresh += 1
                elif grid[row][column] == 0:
                    count_empty += 1
                column += 1
            row += 1
        return count_fresh, count_empty

    def __breadth_first_search(
            self,
            queue: List[List[int]],
            grid: List[List[int]],
            minutes: List[List[int]]) -> List[int]:
        current = None
        while len(queue) > 0:
            current = queue.pop(0)
            if current[0] - 1 >= 0 and grid[current[0] - 1][current[1]] == 1:
                grid[current[0] - 1][current[1]] = 2
                minutes[current[0] - 1][current[1]] = minutes[current[0]][current[1]] + 1
                queue.append([current[0] - 1, current[1]])
            if current[0] + 1 < len(grid) and grid[current[0] + 1][current[1]] == 1:
                grid[current[0] + 1][current[1]] = 2
                minutes[current[0] + 1][current[1]] = minutes[current[0]][current[1]] + 1
                queue.append([current[0] + 1, current[1]])
            if current[1] - 1 >= 0 and grid[current[0]][current[1] - 1] == 1:
                grid[current[0]][current[1] - 1] = 2
                minutes[current[0]][current[1] - 1] = minutes[current[0]][current[1]] + 1
                queue.append([current[0], current[1] - 1])
            if current[1] + 1 < len(grid[0]) and grid[current[0]][current[1] + 1] == 1:
                grid[current[0]][current[1] + 1] = 2
                minutes[current[0]][current[1] + 1] = minutes[current[0]][current[1]] + 1
                queue.append([current[0], current[1] + 1])
        return current

    def oranges_rotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == 0 or grid[0][0] == 2:
                return 0
            else:
                return -1
        queue = self.__find_rotten_oranges(grid)
        if queue is None:
            _, number_empty_cells = self.__count_fresh_oranges(grid)
            if number_empty_cells == len(grid) * len(grid[0]):
                return 0
            return -1
        minutes = [[0 for _ in range(len(row))] for row in grid]
        current = self.__breadth_first_search(queue, grid, minutes)
        number_fresh_oranges, _ = self.__count_fresh_oranges(grid)
        if number_fresh_oranges == 0:
            return minutes[current[0]][current[1]]
        return -1
