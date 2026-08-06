# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    node = TreeNode(val, None, None)
    if not root: return node

    temp = root
    while True:
        if temp.val < val:
            if not temp.right:
                break
            temp = temp.right
        else:
            if not temp.left:
                break
            temp = temp.left

    if val > temp.val:
        temp.right = node
    else:
        temp.left = node

    return root
