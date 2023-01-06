from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    row[i] += 1
                    col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B" and row[i] == 1 and col[j] == 1:
                    res += 1

        return res
