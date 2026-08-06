# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def zigzagLevelOrder(root):
    if not root: return []

    res = []
    st = deque([root])
    level = 0
    while st:
        curr = []
        while st:
            curr += [st.popleft()]
        if level & 1:
            res += [[d.val for d in reversed(curr)]]
        else:
            res += [[d.val for d in curr]]
        for x in curr:
            if x.left:
                st.append(x.left)
            if x.right:
                st.append(x.right)
        level += 1
    return res

def zigzagLevelOrder(root):
    if not root: return []

    res = []
    st = deque([root])
    level = 0
    while st:
        size = len(st)
        curr = [0] * size
        for i in range(size):
            el = st.popleft()
            ind = size - 1 - i if level & 1 else i
            curr[ind] = el.val
            if el.left:
                st.append(el.left)
            if el.right:
                st.append(el.right)
        res += [curr]
        level += 1
    return res
