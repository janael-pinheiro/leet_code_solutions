from typing import List


class Solution:
    def __depth_first_search(self, current: int, is_connected: List[List[int]], visited):
        stack = [current]
        visited[current][current] = 1
        while len(stack) > 0:
            current = stack.pop(0)
            column = 0
            while column < len(is_connected[current]):
                if visited[current][column] == 0 and is_connected[current][column] == 1:
                    stack.insert(0, column)
                    visited[current][column] = 1
                    visited[column][current] = 1
                column += 1

    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        if len(is_connected) == 1:
            if is_connected[0][0] == 1:
                return 1
            return 0
        visited = [[0 for _ in range(len(row))] for row in is_connected]
        number_of_provinces = 0
        row = 0
        while row < len(is_connected):
            column = 0
            while column < len(is_connected[row]):
                if visited[row][column] == 0 and is_connected[row][column] == 1:
                    number_of_provinces += 1
                    self.__depth_first_search(row, is_connected, visited)
                column += 1
            row += 1
        return number_of_provinces
