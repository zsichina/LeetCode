from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 1

        def dfs(root, length):
            nonlocal max_length

            max_length = max(max_length, length)

            if root.left:
                if root.val + 1 == root.left.val:
                    dfs(root.left, length + 1)
                else:
                    dfs(root.left, 1)

            if root.right:
                if root.val + 1 == root.right.val:
                    dfs(root.right, length + 1)
                else:
                    dfs(root.right, 1)

        dfs(root, 1)

        return max_length
