from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(q):
            if q == 0:
                ans.append(matrix1[:])
                return

            for i in range(n):
                if not n-q in rows and not i in cols and not n-q-i in rightDiagonals and not q-i in leftDiagonals:
                    rows.add(n-q)
                    cols.add(i)
                    rightDiagonals.add(n-q-i)
                    leftDiagonals.add(q-i)
                    matrix1.append("."*i+"Q"+"."*(n-i-1))
                    backtrack(q-1)
                    rows.discard(n-q)
                    cols.discard(i)
                    rightDiagonals.discard(n-q-i)
                    leftDiagonals.discard(q-i)
                    matrix1.pop()
            return

        ans = []

        rows = set()
        cols = set()
        rightDiagonals = set()
        leftDiagonals = set()

        matrix = [ "."*n for x in range(n)]
        matrix1 = []
        backtrack(n)

        return ans
