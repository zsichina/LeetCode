from typing import List

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        if n == 1: return 1
        if n <= 3: return 0
        def backtrack(q):
            ans = 0
            for i in range(n):
                if not n-q in rows and not i in cols and not n-q-i in rightDiagonals and not q-i in leftDiagonals:
                    rows.add(n-q)
                    cols.add(i)
                    rightDiagonals.add(n-q-i)
                    leftDiagonals.add(q-i)
                    if q-1==0:
                        ans+=1
                    else:
                        ans+=backtrack(q-1)
                    rows.discard(n-q)
                    cols.discard(i)
                    rightDiagonals.discard(n-q-i)
                    leftDiagonals.discard(q-i)
            return ans

        rows = set()
        cols = set()
        rightDiagonals = set()
        leftDiagonals = set()

        return backtrack(n)
