# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorderTraversal(root):
    out = []

    def recurse(root):
        if root is None:
            return
        recurse(root.left)
        recurse(root.right)
        out.append(root.val)

    recurse(root)

    return out


from collections import deque


def postorderTraversal(root):
    if root == [] or root is None: return []
    stack1 = deque([root])
    stack2 = deque()

    while len(stack1) != 0:
        el = stack1.pop()
        stack2.append(el.val)
        if el.left:
            stack1.append(el.left)
        if el.right:
            stack1.append(el.right)

    return list(stack2)[::-1]
