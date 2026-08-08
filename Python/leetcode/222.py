def countNodes(root):
    if not root:
        return 0

    lh = lefth(root)
    rh = righth(root)
    if lh == rh:
        return 2 ** lh - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)

def lefth(root):
    lh = 0
    if not root:
        return lh
    while root:
        lh += 1
        root = root.left
    return lh

def righth(root):
    rh = 0
    if not root:
        return rh
    while root:
        rh += 1
        root = root.right
    return rh
