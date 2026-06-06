def searchBST(root, val):
    while root is not None:
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
    return None
