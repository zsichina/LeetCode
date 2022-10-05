from typing import  Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def dfs(root, depth):
            if depth == 1:
                temp = root.left
                root.left = TreeNode(val)
                root.left.left = temp

                temp = root.right
                root.right = TreeNode(val)
                root.right.right = temp

            if root.left:
                dfs(root.left, depth-1)

            if root.right:
                dfs(root.right, depth-1)


        dfs(root, depth-1)
        
        return root


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        d = [(root, depth-1)]

        while d:
            node, depth = d.pop()

            if node.left:
                d.append((node.left, depth-1))

            if node.right:
                d.append((node.right, depth-1))

            if depth == 1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp

                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp

        return root