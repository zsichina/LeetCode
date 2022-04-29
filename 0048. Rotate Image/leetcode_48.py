from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def rotate90(n, offset):
            for i in range(n-2*offset):
                matrix[0+offset][i+offset], matrix[i+offset][n-offset], matrix[n-offset][n-i-offset], matrix[n-i-offset][0+offset] = matrix[n-i-offset][0+offset], matrix[0+offset][i+offset], matrix[i+offset][n-offset], matrix[n-offset][n-i-offset]

        n = len(matrix)
        for i in range(n):
            rotate90(n-1, i)
