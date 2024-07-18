class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        good_pair = 0

        def helper(root: TreeNode) -> dict[int, int]:
            nonlocal good_pair
            if not root.left and not root.right:
                return {1: 1}
            ldict, rdict, d = {}, {}, {}
            if root.left:
                ldict = helper(root.left)
            if root.right:
                rdict = helper(root.right)
            for key, val in ldict.items():
                for k, v in rdict.items():
                    if key + k <= distance:
                        good_pair += val * v
            for key, val in ldict.items():
                if key in rdict:
                    rdict[key] += val
                else:
                    rdict[key] = val
            for key, val in rdict.items():
                d[key + 1] = val

            return d

        helper(root)
        return good_pair
