from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j, offset = 0, 0, 0
        m, n = len(matrix), len(matrix[0])
        ans = []

        for _ in range(n * m):
            ans.append(matrix[i][j])
            if i == offset and j + offset < n - 1:
                j += 1
            elif j + offset == n - 1 and i + offset < m - 1:
                i += 1
            elif i + offset == m - 1 and j > offset:
                j -= 1
            elif j == offset and i > offset:
                if i == offset + 1:
                    offset += 1
                    j += 1
                else:
                    i -= 1

        return ans


# class Solution:
#     def spiralOrder(self, matrix):
#         res = []
#         left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

#         while left < right and top < bottom:

#             for i in range(left, right):
#                 res.append(matrix[top][i])
#             top+=1

#             for i in range(top, bottom):
#                 res.append(matrix[i][right-1])
#             right-=1

#             if left >= right or top >= bottom:
#                 break

#             for i in range(right-1, left-1, -1):
#                 res.append(matrix[bottom-1][i])
#             bottom-=1

#             for i in range(bottom-1, top-1, -1):
#                 res.append(matrix[i][left])
#             left+=1

#         return res
