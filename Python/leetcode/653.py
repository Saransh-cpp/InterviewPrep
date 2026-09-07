# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIteratorNext:

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


class BSTIteratorBefore:

    def __init__(self, root):
        self.st = deque()
        while root:
            self.st.append(root)
            root = root.right

    def before(self) -> int:
        el = self.st.pop()
        ret_val = el.val
        if el.left:
            self.st.append(el.left)
            el = el.left.right
            while el:
                self.st.append(el)
                el = el.right
        return ret_val

    def hasNext(self) -> bool:
        return len(self.st) != 0


def findTarget(root, k):
    left = BSTIteratorNext(root)
    right = BSTIteratorBefore(root)
    left_val = left.next()
    right_val = right.before()
    while left_val < right_val:
        if left_val + right_val == k:
            return True
        elif left_val + right_val < k:
            left_val = left.next()
        else:
            right_val = right.before()
    return False
