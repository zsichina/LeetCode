import math
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [None] * (len(books) + 1)

        def helper(books, idx):
            if dp[idx] is not None:
                return dp[idx]
            if idx == len(books):
                return 0
            row_height, width, min_height = 0, 0, math.inf
            while idx < len(books):
                if width + books[idx][0] > shelfWidth:
                    break
                width += books[idx][0]
                row_height = max(row_height, books[idx][1])
                idx += 1
                dp[idx] = helper(books, idx)
                min_height = min(row_height + dp[idx], min_height)
            return min_height

        return helper(books, 0)


sol = Solution()
print(sol.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
print(sol.minHeightShelves([[1, 1], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
