from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal max_sum

            sm = root.val

            left_sum = 0
            if root.left:
                left_sum = dfs(root.left)

            right_sum = 0
            if root.right:
                right_sum = dfs(root.right)

            max_sum = max(max_sum, sm, sm + left_sum, sm + right_sum, sm + left_sum + right_sum)

            return max(sm, sm + left_sum, sm + right_sum)

        max_sum = -1000
        dfs(root)

        return max_sum
