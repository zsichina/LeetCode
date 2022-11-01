from typing import List
from functools import lru_cache


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        @lru_cache
        def find_path(row, col):
          if row == m:
            return col

          if grid[row][col] == 1:
            if col+1 == n or grid[row][col+1] == -1:
              return -1
            else:
              col+=1
          else:
            if col-1 < 0 or grid[row][col-1] == 1:
              return -1
            else:
              col-=1

          return find_path(row+1, col)

        res = []
        for i in range(n):
          res.append(find_path(0, i))

        return res
