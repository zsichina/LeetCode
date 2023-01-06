from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root, dp, odd_nums):
            nonlocal ans
            if root.val in dp:
                if dp[root.val] % 2 == 0:
                    odd_nums += 1
                else:
                    odd_nums -= 1
                dp[root.val] += 1
            else:
                dp[root.val] = 1
                odd_nums += 1

            if root.left:
                dfs(root.left, dp, odd_nums)

            if root.right:
                dfs(root.right, dp, odd_nums)

            if not root.left and not root.right and odd_nums < 2:
                ans += 1

            dp[root.val] -= 1
            if dp[root.val] % 2 == 0:
                odd_nums -= 1
            else:
                odd_nums += 1
            # if dp[root.val] == 0:
            #     del dp[root.val]

        dp = {}
        ans = 0
        dfs(root, dp, 0)

        return ans
