from typing import List


class Solution:
    def __update_matrix_column(self, matrix: List[List[int]], column: int) -> None:
        row = 0
        while row < len(matrix):
            matrix[row][column] = 0
            row += 1

    def __update_matrix_row(self, matrix: List[List[int]], row: int) -> None:
        column = 0
        while column < len(matrix[row]):
            matrix[row][column] = 0
            column += 1

    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        already_seen_columns = []
        rows = set()
        columns = set()
        row = 0
        while row < len(matrix):
            column = 0
            while column < len(matrix[row]):
                if matrix[row][column] == 0:
                    rows.add(row)
                    columns.add(column)
                column += 1
            row += 1

        for row in rows:
            self.__update_matrix_row(matrix, row)
        for column in columns:
            self.__update_matrix_column(matrix, column)
