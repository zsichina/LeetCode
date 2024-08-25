from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c) -> int:
            l_diag = r_diag = 0
            seen = set()
            for i in range(3):
                row_sum = col_sum = 0
                for j in range(3):
                    row_sum += grid[r + i][c + j]
                    col_sum += grid[r + j][c + i]
                    if grid[r + i][c + j] in seen:
                        return 0
                    if not 1 <= grid[r + i][c + j] <= 9:
                        return 0
                    seen.add(grid[r + i][c + j])
                if row_sum != 15 or col_sum != 15:
                    return 0
                l_diag += grid[r + i][c + i]
                r_diag += grid[r + i][c + 2 - i]
            return 1 if l_diag == 15 and r_diag == 15 else 0

        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        total = 0
        for r in range(m - 3 + 1):
            for c in range(n - 3 + 1):
                total += is_magic(r, c)

        return total
