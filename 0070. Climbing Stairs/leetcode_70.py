from functools import lru_cache

class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(n):
            if n <=1: return 1

            if n-1 not in dp:
                dp[n-1] = dfs(n-1)
            if n-2 not in dp:
                dp[n-2] = dfs(n-2)
            return dp[n-1] + dp[n-2]

        return dfs(n)

class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if n <=1: return 1

        if n-1 not in self.dp:
            self.dp[n-1] = self.climbStairs(n-1)
        if n-2 not in self.dp:
            self.dp[n-2] = self.climbStairs(n-2)
        return self.dp[n-1] + self.dp[n-2]

        return self.climbStairs(n)
