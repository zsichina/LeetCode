from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            s = str(root.val)

            if root.left:
                s += "(" + dfs(root.left) + ")"
            elif root.right:
                s += "()"

            if root.right:
                s += "(" + dfs(root.right) + ")"

            return s

        return dfs(root)
