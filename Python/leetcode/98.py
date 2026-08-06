# or inorder traversal and check if it is sorted
def isValidBST(root):
    return recurse(root, -float("inf"), float("inf"))

def recurse(root, low, high):
    if not root:
        return True
    if low >= root.val or high <= root.val:
        return False
    return recurse(root.left, low, root.val) and recurse(root.right, root.val, high)
