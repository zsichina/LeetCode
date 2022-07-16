from typing import List
from collections import deque

# DFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = "0"
            for r, c in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if 0 <= r <= m-1 and 0 <= c <= n-1 and grid[r][c] == "1":
                    dfs(r, c)

        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
                
        return cnt

# Iterative solution with stack
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    stack.append((i,j))
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = "0"
                        for r, c in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                            if 0 <= r <= m-1 and 0 <= c <= n-1 and grid[r][c] == "1":
                                stack.append((r,c))
                
        return cnt


# BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        d = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    grid[i][j] = "0"
                    d.append((i,j))
                    while d:
                        row, col = d.popleft()
                        for r, c in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                            if 0 <= r <= m-1 and 0 <= c <= n-1 and grid[r][c] == "1":
                                grid[r][c] = "0"
                                d.append((r,c))
        return cnt

