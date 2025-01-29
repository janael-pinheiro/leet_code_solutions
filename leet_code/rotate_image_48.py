from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        right_border = len(matrix[0]) - 1
        lower_border = len(matrix) - 1
        left_border = 0
        upper_border = 0
        pointer = 0
        while (upper_border + pointer < lower_border - pointer) and (left_border + pointer < right_border - pointer):
            column = pointer
            while column < right_border - pointer:
                temp = matrix[upper_border+column][right_border-pointer]
                matrix[upper_border+column][right_border-pointer] = matrix[upper_border+pointer][column]
                temp2 = matrix[lower_border-pointer][right_border-column]
                matrix[lower_border-pointer][right_border-column] = temp
                temp3 = matrix[lower_border-column][left_border+pointer]
                matrix[lower_border-column][left_border+pointer] = temp2
                matrix[upper_border+pointer][left_border+column] = temp3
                column += 1
            pointer += 1
