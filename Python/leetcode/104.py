# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def maxDepth(root):
    if not root: return 0

    q = deque([root])
    count = 0
    while q:
        curr = []
        while q:
            curr += [q.popleft()]
        for x in curr:
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        count += 1
    return count

def maxDepth(root):
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
