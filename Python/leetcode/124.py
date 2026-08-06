# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_sum = -float("inf")

def path_sum(root):
    if not root:
        return 0
    ls = max(0, path_sum(root.left))
    rs = max(0, path_sum(root.right))
    max_sum = max(max_sum, root.val + ls + rs)
    return root.val + max(ls, rs)

def maxPathSum(root):
    path_sum(root)
    return max_sum
