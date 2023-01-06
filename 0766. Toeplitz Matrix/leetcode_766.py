from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(1, min(m - i, n)):
                if matrix[i + j][j] != matrix[i][0]:
                    return False

        for j in range(1, n):
            for i in range(1, min(m, n - j)):
                if matrix[i][j + i] != matrix[0][j]:
                    return False

        return True
