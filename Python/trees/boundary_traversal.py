# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

def traverse_left(root, nums):
    if not root or (not root.left and not root.right):
        return
    nums += [root.data]
    if root.left:
        traverse_left(root.left, nums)
    elif root.right:
        traverse_left(root.right, nums)

def traverse_right(root, nums):
    if not root or (not root.left and not root.right):
        return
    nums += [root.data]
    if root.right:
        traverse_right(root.right, nums)
    elif root.left:
        traverse_right(root.left, nums)

def traverse_leaves(root, nums):
    if not root.left and not root.right:
        nums += [root.data]
        return
    if root.left:
        traverse_leaves(root.left, nums)
    if root.right:
        traverse_leaves(root.right, nums)

def boundary(root):
    nums = []

    if not root: return []
    if root.left or root.right:
        nums += [root.data]

    traverse_left(root.left, nums)
    traverse_leaves(root, nums)
    right_nums = []
    traverse_right(root.right, right_nums)
    return nums + right_nums[::-1]
