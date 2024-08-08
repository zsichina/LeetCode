from typing import List


from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        res = []
        corners = 4 if (rows > 1 and cols > 1) else 2 if rows > 1 or cols > 1 else 1
        change = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction, steps, remaining, visited_corners = 0, 1, 1, 0
        while visited_corners != corners:
            if 0 <= rStart < rows and 0 <= cStart < cols:
                res.append([rStart, cStart])
            if rStart in (0, rows - 1) and cStart in (0, cols - 1):
                visited_corners += 1
            rStart += change[direction][0]
            cStart += change[direction][1]
            remaining -= 1
            if remaining == 0:
                steps += direction % 2
                direction = (direction + 1) % 4
                remaining = steps

        return res
