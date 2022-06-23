'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j, offset = 0, 0, 0
        for num in range(n*n):
            matrix[i][j] = num + 1
            if i == offset and j + offset < n-1:
                j+=1
            elif j + offset == n-1 and i + offset < n-1:
                i+=1
            elif i + offset == n-1 and j > offset:
                j-=1
            elif j == offset and i > offset:
                if i == offset + 1:
                    offset +=1
                    j+=1
                else:
                    i-=1
        return matrix


if __name__ == "__main__":
    sol = Solution()

    print("OK" if sol.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]] else "Error")
    print("OK" if sol.generateMatrix(1) == [[1]] else "Error")
    print("OK" if sol.generateMatrix(5) == [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]] else "Error")

