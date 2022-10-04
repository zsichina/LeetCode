from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        targetSum -= root.val
        
        if targetSum == 0 and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        d = [(root, targetSum-root.val)]

        while d:
            node, val = d.pop()
            if val == 0 and not node.left and not node.right:
                return True

            if node.left:
                d.append((node.left, val-node.left.val))

            if node.right:
                d.append((node.right, val-node.right.val))

        return False
