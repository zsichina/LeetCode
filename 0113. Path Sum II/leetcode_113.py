from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(root, sm, lst):
            sm += root.val
            lst.append(root.val)
            if root.left:
                dfs(root.left, sm, lst)
            if root.right:
                dfs(root.right, sm, lst)

            if not root.left and not root.right and sm == targetSum:
                res.append(lst[:])
            lst.pop()

        res = []
        dfs(root, 0, [])

        return res
