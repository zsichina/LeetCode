from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return 1
        if n <= 3:
            return 0

        def backtrack(q):
            ans = 0
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
                    if q - 1 == 0:
                        ans += 1
                    else:
                        ans += backtrack(q - 1)
                    rows.discard(n - q)
                    cols.discard(i)
                    rightDiagonals.discard(n - q - i)
                    leftDiagonals.discard(q - i)
            return ans

        rows = set()
        cols = set()
        rightDiagonals = set()
        leftDiagonals = set()

        return backtrack(n)


class Solution:
    def __init__(self):
        self.under_attack_cols = set()
        self.ua_diag = set()
        self.ua_anti_diag = set()

    def add_under_attack(self, row, col):
        self.under_attack_cols.add(col)
        self.ua_diag.add(row - col)
        self.ua_anti_diag.add(row + col)

    def remove_under_attack(self, row, col):
        self.under_attack_cols.remove(col)
        self.ua_diag.remove(row - col)
        self.ua_anti_diag.remove(row + col)

    def is_under_attack(self, row, col):
        if col in self.under_attack_cols or row - col in self.ua_diag or row + col in self.ua_anti_diag:
            return True
        return False

    def backtracking(self, row):
        if row == self.n:
            return 1

        res = 0
        for col in range(self.n):
            if not self.is_under_attack(row, col):
                self.add_under_attack(row, col)
                res += self.backtracking(row + 1)
                self.remove_under_attack(row, col)

        return res

    def totalNQueens(self, n: int) -> int:
        self.n = n
        return self.backtracking(0)
