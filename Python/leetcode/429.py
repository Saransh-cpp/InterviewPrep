"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque


def levelOrder(root):
    if not root: return []

    q = deque([root])
    res = []
    while q:
        curr = []
        size = len(q)
        for i in range(size):
            el = q.popleft()
            curr += [el.val]
            for child in el.children:
                q.append(child)
        res += [curr]
    return res
