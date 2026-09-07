# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root, p, q):
    if not root:
        return
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    return root
