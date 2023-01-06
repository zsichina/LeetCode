class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if p.val > q.val:
            p, q = q, p

        def dfs(root):
            if p.val <= root.val <= q.val:
                return root
            elif q.val < root.val:
                return dfs(root.left)
            else:
                return dfs(root.right)

        return dfs(root)


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if p.val > q.val:
            p, q = q, p

        node = root
        while node:
            if p.val <= node.val <= q.val:
                return node
            elif q.val < node.val:
                node = node.left
            else:
                node = node.right
