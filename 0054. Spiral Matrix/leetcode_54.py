from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j, offset = 0, 0, 0
        m, n = len(matrix), len(matrix[0])
        ans = []
        
        for _ in range(n*m):
            ans.append(matrix[i][j])
            if i==offset and j+offset<n-1:
                j+=1
            elif j+offset==n-1 and i+offset<m-1:
                i+=1
            elif i+offset==m-1 and j>offset:
                j-=1
            elif j==offset and i>offset:
                if i==offset+1:
                    offset+=1
                    j+=1
                else:
                    i-=1

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



if __name__ == '__main__':
    sol = Solution()
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("OK" if sol.spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5] else "Error")
    
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print("OK" if sol.spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7] else "Error")
    
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    print("OK" if sol.spiralOrder(matrix) == [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13] else "Error")
