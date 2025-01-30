from typing import List


class Solution:
    def __update_board(
            self,
            board: List[List[int]],
            temp_board: List[List[int]]) -> None:
        row = 0
        while row < len(board):
            column = 0
            while column < len(board[row]):
                board[row][column] = temp_board[row][column]
                column += 1
            row += 1

    def __update_state(
            self,
            board: List[List[int]],
            temp_board: List[List[int]],
            row: int,
            column: int,
            sum_neighbors: int) -> None:
        if board[row][column] == 1 and sum_neighbors < 2:
            temp_board[row][column] = 0
        elif board[row][column] == 1 and sum_neighbors <= 3:
            temp_board[row][column] = 1
        elif board[row][column] == 1 and sum_neighbors > 3:
            temp_board[row][column] = 0
        elif board[row][column] == 0 and sum_neighbors == 3:
            temp_board[row][column] = 1

    def __update_row(self, n: int, board: List[List[int]], temp_board: List[List[int]]):
        column = 0
        while column < n:
            sum_neighbors = 0
            if column != 0 and column != len(board[0]) - 1:
                sum_neighbors = board[0][column - 1] + board[0][column + 1]
            self.__update_state(board, temp_board, 0, column, sum_neighbors)
            column += 1
        self.__update_board(board, temp_board)

    def __update_column(self, m: int, board: List[List[int]], temp_board: List[List[int]]):
        row = 0
        while row < m:
            sum_neighbors = 0
            if row != 0 and row != m - 1:
                sum_neighbors = board[row - 1][0] + board[row + 1][0]
            self.__update_state(board, temp_board, row, 0, sum_neighbors)
            row += 1
        self.__update_board(board, temp_board)

    def game_of_life(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        temp_board = [[0] * n for _ in range(m)]

        if m == 1:
            self.__update_row(n, board, temp_board)
            return

        if n == 1:
            self.__update_column(m, board, temp_board)
            return

        row = 0
        while row < m:
            column = 0
            while column < n:
                if row == 0 and column == 0:
                    sum_neighbors = board[row][column + 1] + board[row + 1][column + 1] + board[row + 1][column]
                elif row == 0 and column == n - 1:
                    sum_neighbors = board[row][column - 1] + board[row + 1][column - 1] + board[row + 1][column]
                elif row == m - 1 and column == n - 1:
                    sum_neighbors = board[row][column - 1] + board[row - 1][column - 1] + board[row - 1][column]
                elif row == m - 1 and column == 0:
                    sum_neighbors = board[row - 1][column] + board[row - 1][column + 1] + board[row][column + 1]
                elif row == 0:
                    sum_neighbors = board[row][column-1] + board[row+1][column-1] + board[row+1][column] + board[row+1][column+1] + board[row][column+1]
                elif row == m - 1:
                    sum_neighbors = board[row][column - 1] + board[row - 1][column - 1] + board[row - 1][column] + \
                                    board[row - 1][column + 1] + board[row][column + 1]
                elif column == 0:
                    sum_neighbors = board[row-1][column] + board[row - 1][column + 1] + board[row][column+1] + \
                                    board[row + 1][column + 1] + board[row+1][column]
                elif column == n - 1:
                    sum_neighbors = board[row - 1][column] + board[row - 1][column - 1] + board[row][column-1] + \
                                    board[row + 1][column - 1] + board[row + 1][column]
                else:
                    sum_neighbors = board[row-1][column] + board[row-1][column-1] + board[row][column-1] + board[row+1][column-1] + board[row+1][column] + board[row+1][column+1] + board[row][column+1] + board[row-1][column+1]
                self.__update_state(board, temp_board, row, column, sum_neighbors)
                column += 1
            row += 1
        self.__update_board(board, temp_board)
