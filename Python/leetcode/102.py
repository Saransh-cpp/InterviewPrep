# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(root):
        if root is None: return []

        q = deque()
        q.append(root)
        out = []
        while len(q) > 0:
            subout = []
            size = len(q)
            for i in range(size):
                el = q.popleft()
                if el.left is not None: q.append(el.left)
                if el.right is not None: q.append(el.right)
                subout.append(el.val)
            out.append(subout)
        return out
