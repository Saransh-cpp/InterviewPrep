# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if not root:
        return True 
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def height(root):
    if not root: return 0
    lh = height(root.left)
    rh = height(root.right)
    if lh == -1 or rh == -1 or abs(lh - rh) > 1: return -1
    return 1 + max(lh, rh)

def isBalanced(root):
    return height(root) != -1
