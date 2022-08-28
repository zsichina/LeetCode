from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            diag = []
            for j in range(min(m-i, n)):
                diag.append(mat[i+j][j])
            diag.sort(reverse=True)
            for j in range(min(m-i, n)):
                mat[i+j][j] = diag.pop()

        for j in range(1, n):
            diag = []
            for i in range(min(m, n-j)):
                diag.append(mat[i][j+i])
            diag.sort(reverse=True)
            for i in range(min(m, n-j)):
                mat[i][j+i] = diag.pop()

        return mat
