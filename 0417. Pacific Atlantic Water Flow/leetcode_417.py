from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        res = []

        def dfs(row, col, pacific, atlantic):
            if pacific and dp[row][col][0] or atlantic and dp[row][col][1]:
                return

            if pacific:
                dp[row][col][0] = True

            if atlantic:
                dp[row][col][1] = True

                if dp[row][col][0]:
                    res.append([row, col])

            for r, c in ((row-1, col), (row, col-1), (row+1, col), (row, col+1)):
                if 0 <= r <= m-1 and 0 <= c <= n-1 and heights[r][c] >= heights[row][col]:
                    dfs(r, c, pacific, atlantic)
            

        dp = [[[False, False] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dfs(i, 0, True, False)

        for j in range(n):
            dfs(0, j, True, False)

        for i in range(m):
            dfs(i, n-1, False, True)

        for j in range(n):
            dfs(m-1, j, False, True)

        return res
