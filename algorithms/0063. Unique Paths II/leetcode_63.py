from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            matrix[i][0] = 0 if matrix[i - 1][0] == 0 else [1, 0][obstacleGrid[i][0]]

        for j in range(n):
            matrix[0][j] = 0 if matrix[0][j - 1] == 0 else [1, 0][obstacleGrid[0][j]]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = 0 if obstacleGrid[i][j] == 1 else matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        row = [[1, 0][obstacleGrid[0][0]]]

        for i in range(1, n):
            if obstacleGrid[0][i] == 0 and row[i - 1] == 1:
                row.append(1)
            else:
                row.append(0)

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    if j > 0:
                        row[j] += row[j - 1]

        return row[n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}

        def makeStep(i, j):
            if i > m - 1 or j > n - 1 or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1

            if not (i + 1, j) in dp:
                dp[(i + 1, j)] = makeStep(i + 1, j)
            if not (i, j + 1) in dp:
                dp[(i, j + 1)] = makeStep(i, j + 1)

            if i < m - 1 or j < n - 1:
                return dp[(i + 1, j)] + dp[(i, j + 1)]

        return makeStep(0, 0)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m - 1][n - 1]
