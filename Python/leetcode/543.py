max_height = 0

def height(root):
    if not root:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    max_height = max(max_height, lh + rh)
    return 1 + max(lh, rh)

def diameterOfBinaryTree(root):
    height(root)
    return max_height
