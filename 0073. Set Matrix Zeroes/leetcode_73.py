from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = [set(), set()]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros[0].add(i)
                    zeros[1].add(j)

        for i in zeros[0]:
            for j in range(n):
                matrix[i][j] = 0

        for j in zeros[1]:
            for i in range(m):
                matrix[i][j] = 0

        print(matrix)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_first_col = 0

        for i in range(m):
            if matrix[i][0] == 0:
                set_first_col = 1
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if set_first_col:
            for i in range(m):
                matrix[i][0] = 0

