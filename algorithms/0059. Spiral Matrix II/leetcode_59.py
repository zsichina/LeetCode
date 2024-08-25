from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j, offset = 0, 0, 0
        for num in range(n * n):
            matrix[i][j] = num + 1
            if i == offset and j + offset < n - 1:
                j += 1
            elif j + offset == n - 1 and i + offset < n - 1:
                i += 1
            elif i + offset == n - 1 and j > offset:
                j -= 1
            elif j == offset and i > offset:
                if i == offset + 1:
                    offset += 1
                    j += 1
                else:
                    i -= 1
        return matrix
