# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSymmetric(root):
    return recurse(root.left, root.right)

def recurse(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    return (
        recurse(left.left, right.right)
        and recurse(left.right, right.left)
    )
