class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            ans = 0
            if root.val >= max_val:
                ans = 1

            if root.left:
                ans += dfs(root.left, max(root.left.val, max_val))

            if root.right:
                ans += dfs(root.right, max(root.right.val, max_val))

            return ans

        return dfs(root, root.val)
