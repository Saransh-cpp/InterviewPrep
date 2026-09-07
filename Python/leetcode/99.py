# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = TreeNode(-float("inf"))

    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.recurse(root, res)
        res[0].val, res[-1].val = res[-1].val, res[0].val

    def recurse(self, root, res):
        if not root:
            return
        self.recurse(root.left, res)
        if self.prev and self.prev.val > root.val:
            res += [self.prev, root]
        self.prev = root
        self.recurse(root.right, res)
