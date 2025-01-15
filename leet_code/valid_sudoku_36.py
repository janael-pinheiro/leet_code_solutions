from typing import List


class Solution:
    def __search_sub_boxes(self, board: List[List[str]]) -> bool:
        row = 0
        while row < len(board):
            column = 0
            while column < len(board[row]):
                sub_row = 0
                values = set()
                while sub_row < 3:
                    sub_column = 0
                    while sub_column < 3:
                        current = board[row + sub_row][column + sub_column]
                        if current == '.':
                            sub_column += 1
                            continue
                        if current in values:
                            return False
                        values.add(current)
                        sub_column += 1
                    sub_row += 1
                column += 3
            row += 3
        return True

    def __scan_row_level(self, board: List[List[str]]):
        row_number = 0
        while row_number < len(board):
            column_number = 0
            row_values = set()
            while column_number < len(board[row_number]):
                current = board[row_number][column_number]
                if current == '.':
                    column_number += 1
                    continue
                if current in row_values:
                    return False
                row_values.add(current)
                column_number += 1
            row_number += 1
        return True

    def __scan_column_level(self, board: List[List[str]]):
        column_number = 0
        while column_number < len(board):
            row_number = 0
            column_values = set()
            while row_number < len(board):
                current = board[row_number][column_number]
                if current == '.':
                    row_number += 1
                    continue
                if current in column_values:
                    return False
                column_values.add(current)
                row_number += 1
            column_number += 1
        return True

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        if self.__search_sub_boxes(board):
            return self.__scan_row_level(board) and self.__scan_column_level(board)
        return False
