from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        limit = len(matrix) * len(matrix[0])
        output = []
        left_border = -1
        right_border = len(matrix[0])
        upper_border = -1
        lower_border = len(matrix)
        index = 0
        column = -1
        row = -1
        while index < limit:
            upper_border += 1
            column += 1
            row += 1

            while column < right_border and index < limit:
                output.append(matrix[row][column])
                column += 1
                index += 1

            right_border -= 1
            row += 1
            column -= 1
            while row < lower_border and index < limit:
                output.append(matrix[row][column])
                row += 1
                index += 1

            lower_border -= 1
            column -= 1
            row -= 1
            while column > left_border and index < limit:
                output.append(matrix[row][column])
                column -= 1
                index += 1

            left_border += 1
            row -= 1
            column += 1
            while row > upper_border and index < limit:
                output.append(matrix[row][column])
                row -= 1
                index += 1

        return output
