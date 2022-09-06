from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            found = found_left = found_right = False
            if root.val == 1:
                found = True

            if root.left:
                found_left = dfs(root.left)
                if not found_left:
                    root.left = None

            if root.right:
                found_right = dfs(root.right)
                if not found_right:
                    root.right = None

            return found or found_left or found_right

        found = dfs(root)

        if not found:
            return None
        else:
            return root
