from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(q):
            if q == 0:
                ans.append(matrix[:])
                return

            for i in range(n):
                if (
                    n - q not in rows
                    and i not in cols
                    and n - q - i not in rightDiagonals
                    and q - i not in leftDiagonals
                ):
                    rows.add(n - q)
                    cols.add(i)
                    rightDiagonals.add(n - q - i)
                    leftDiagonals.add(q - i)
                    matrix.append("." * i + "Q" + "." * (n - i - 1))
                    backtrack(q - 1)
                    rows.discard(n - q)
                    cols.discard(i)
                    rightDiagonals.discard(n - q - i)
                    leftDiagonals.discard(q - i)
                    matrix.pop()
            return

        ans = []

        rows = set()
        cols = set()
        rightDiagonals = set()
        leftDiagonals = set()

        matrix = []
        backtrack(n)

        return ans
