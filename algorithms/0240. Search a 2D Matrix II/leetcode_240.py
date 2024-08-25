from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n - 1]:
                start, end = 0, n - 1

                while start <= end:
                    mid = (start + end) // 2

                    if matrix[i][mid] < target:
                        start = mid + 1
                    elif matrix[i][mid] > target:
                        end = mid - 1
                    else:
                        return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        row, col = m - 1, 0

        while row >= 0 and col <= n - 1:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False
