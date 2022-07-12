from functools import lru_cache

class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        if n < 1:
            return 1
        cnt = 0
        for i in range(n):
            cnt += self.numTrees(i) * self.numTrees(n-(i+1))
        return cnt

class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0: 1}

        for i in range(1, n+1):
            for j in range(0, i):
                if i not in dp:
                    dp[i] = 0
                dp[i] += dp[j]*dp[i-j-1]

        return dp[n]
