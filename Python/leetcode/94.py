# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
    out = []

    def recurse(root):
        if root is None:
            return
        recurse(root.left)
        out.append(root.val)
        recurse(root.right)

    recurse(root)

    return out


from collections import deque


def inorderTraversal(root):
    stack = deque()
    node = root
    out = []

    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            out.append(node.val)
            node = node.right

    return out
