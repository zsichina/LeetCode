from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            diag = []
            for j in range(min(m - i, n)):
                diag.append(mat[i + j][j])
            diag.sort(reverse=True)
            for j in range(min(m - i, n)):
                mat[i + j][j] = diag.pop()

        for j in range(1, n):
            diag = []
            for i in range(min(m, n - j)):
                diag.append(mat[i][j + i])
            diag.sort(reverse=True)
            for i in range(min(m, n - j)):
                mat[i][j + i] = diag.pop()

        return mat


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        def sortDiagonal(row, col):
            diag = []
            diag_len = min(m - row, n - col)

            for i in range(diag_len):
                diag.append(mat[row + i][col + i])

            heapify(diag)

            for i in range(diag_len):
                mat[row + i][col + i] = heappop(diag)

        for row in range(m):
            sortDiagonal(row, 0)

        for col in range(1, n):
            sortDiagonal(0, col)

        return mat


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        def sortDiagonal(row, col):
            diag = []
            diag_len = min(m - row, n - col)

            for i in range(diag_len):
                diag.append(mat[row + i][col + i])

            diag = countingSort(diag)

            for i in range(diag_len):
                mat[row + i][col + i] = diag[i]

        def countingSort(nums):
            minimum = 1
            maximum = 100

            counts = Counter(nums)

            sorted_nums = []
            for i in range(minimum, maximum + 1):
                sorted_nums.extend([i] * counts[i])
            return sorted_nums

        for row in range(m):
            sortDiagonal(row, 0)

        for col in range(1, n):
            sortDiagonal(0, col)

        return mat
