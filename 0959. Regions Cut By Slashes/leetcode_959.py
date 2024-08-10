from typing import List


class Solution:

    def dfs(self, i, j, n):
        self.matrix[i][j] = 1
        for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= a < 3 * n and 0 <= b < 3 * n and self.matrix[a][b] == 0:
                self.dfs(a, b, n)

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        self.matrix = [[0] * 3 * n for _ in range(3 * n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    for k in range(3):
                        self.matrix[i * 3 + k][j * 3 + 2 - k] = 1
                if grid[i][j] == "\\":
                    for k in range(3):
                        self.matrix[i * 3 + k][j * 3 + k] = 1

        regions = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if self.matrix[i][j] == 0:
                    self.dfs(i, j, n)
                    regions += 1
        return regions
