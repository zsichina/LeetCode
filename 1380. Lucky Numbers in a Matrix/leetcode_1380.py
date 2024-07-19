import math
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = [math.inf for _ in range(len(matrix))]
        maxs = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mins[i] = min(mins[i], matrix[i][j])
                maxs[j] = max(maxs[j], matrix[i][j])

        return list(set(mins).intersection(set(maxs)))
