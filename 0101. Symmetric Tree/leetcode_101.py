from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):

            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            if not dfs(left.left, right.right) or not dfs(left.right, right.left):
                return False

            return True

        return dfs(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = [root.left]
        right = [root.right]

        while left or right:

            left_node = left.pop()
            right_node = right.pop()

            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            left.append(left_node.left)
            left.append(left_node.right)
            right.append(right_node.right)
            right.append(right_node.left)

        return True
