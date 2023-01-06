from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def rotate90(n, offset):
            for i in range(n - 2 * offset):
                (
                    matrix[0 + offset][i + offset],
                    matrix[i + offset][n - offset],
                    matrix[n - offset][n - i - offset],
                    matrix[n - i - offset][0 + offset],
                ) = (
                    matrix[n - i - offset][0 + offset],
                    matrix[0 + offset][i + offset],
                    matrix[i + offset][n - offset],
                    matrix[n - offset][n - i - offset],
                )

        n = len(matrix)
        for i in range(n):
            rotate90(n - 1, i)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        offset = 0
        while n - 2 * offset > 1:
            for i in range(n - 1 - 2 * offset):
                matrix[offset][offset + i], matrix[n - 1 - offset - i][offset] = (
                    matrix[n - 1 - offset - i][offset],
                    matrix[offset][offset + i],
                )
                (matrix[n - 1 - offset - i][offset], matrix[n - 1 - offset][n - 1 - offset - i],) = (
                    matrix[n - 1 - offset][n - 1 - offset - i],
                    matrix[n - 1 - offset - i][offset],
                )
                (matrix[n - 1 - offset][n - 1 - offset - i], matrix[offset + i][n - 1 - offset],) = (
                    matrix[offset + i][n - 1 - offset],
                    matrix[n - 1 - offset][n - 1 - offset - i],
                )

            offset += 1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        offset = 0
        while n - 2 * offset > 1:
            for i in range(n - 1 - 2 * offset):
                temp = matrix[offset][offset + i]
                matrix[offset][offset + i] = matrix[n - 1 - offset - i][offset]
                matrix[n - 1 - offset - i][offset] = matrix[n - 1 - offset][n - 1 - offset - i]
                matrix[n - 1 - offset][n - 1 - offset - i] = matrix[offset + i][n - 1 - offset]
                matrix[offset + i][n - 1 - offset] = temp

            offset += 1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
