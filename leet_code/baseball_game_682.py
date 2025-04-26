from typing import List


class Solution:
    def cal_points(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                record.append(record[-1] * 2)
            elif operation == 'C':
                record.pop(-1)
            else:
                record.append(int(operation))
        return sum(record)
