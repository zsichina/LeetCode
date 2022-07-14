from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        col_start, col_end  = 0, m - 1
        while col_start <= col_end:
            col_mid = col_start + (col_end - col_start)//2
            if target < matrix[col_mid][0]:
                col_end = col_mid - 1
            elif target > matrix[col_mid][n-1]:
                col_start = col_mid + 1
            else:
                row_start, row_end = 0, n - 1
                while row_start <= row_end:
                    mid_row = row_start + (row_end-row_start)//2
                    if target < matrix[col_mid][mid_row]:
                        row_end = mid_row - 1
                    elif target > matrix[col_mid][mid_row]:
                        row_start = mid_row + 1
                    else:
                        return True
                break

        return False



class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        start, end = 0, m*n - 1
        while start < end:
            mid = (start + end)//2
            if matrix[mid//m][mid%m] < target:
                start = mid + 1
            else:
                end = mid
        return matrix[start//m][start%m] == target
