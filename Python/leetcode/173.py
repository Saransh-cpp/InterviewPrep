# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIterator:

    def __init__(self, root):
        self.st = deque()
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        el = self.st.pop()
        ret_val = el.val
        if el.right:
            self.st.append(el.right)
            el = el.right.left
            while el:
                self.st.append(el)
                el = el.left
        return ret_val

    def hasNext(self) -> bool:
        return len(self.st) != 0
