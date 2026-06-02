# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderTraversal(root):
    out = []

    def recurse(root):
        if root is None:
            return
        out.append(root.val)
        recurse(root.left)
        recurse(root.right)

    recurse(root)

    return out


from collections import deque


def preorderTraversal(root):
    if root == [] or root is None: return []
    stack = deque([root])
    out = []

    while len(stack) != 0:
        el = stack.pop()
        out.append(el.val)
        if el.right:
            stack.append(el.right)
        if el.left:
            stack.append(el.left)

    return out
