class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for x in range(n)] for y in range(m)]

        for i in range(m):
            matrix[i][0] = 1

        for j in range(n):
            matrix[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for x in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]

        return row[n - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def makeStep(i, j):
            if i == m - 1 or j == n - 1:
                dp[(i, j)] = 1
                return 1
            if i < m - 1 and j < n - 1:
                if not (i + 1, j) in dp:
                    dp[(i + 1, j)] = makeStep(i + 1, j)
                if not (i, j + 1) in dp:
                    dp[(i, j + 1)] = makeStep(i, j + 1)
                return dp[(i + 1, j)] + dp[(i, j + 1)]
            return 0

        return makeStep(0, 0)
