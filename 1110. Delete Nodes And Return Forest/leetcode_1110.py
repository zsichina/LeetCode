from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)

        def helper(
            root: Optional[TreeNode], to_delete: set[int], has_parent: bool = False
        ) -> List[TreeNode]:
            forest: List[TreeNode] = []
            if not root:
                return forest
            if root.val not in to_delete_set:
                if has_parent is False:
                    forest.append(root)
                has_parent = True
            else:
                has_parent = False
            left, right = root.left, root.right
            if left:
                if left.val in to_delete_set:
                    root.left = None
                forest.extend(helper(left, to_delete, has_parent))
            if right:
                if right.val in to_delete_set:
                    root.right = None
                forest.extend(helper(right, to_delete, has_parent))

            return forest

        return helper(root, to_delete_set, False)
