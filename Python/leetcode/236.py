def lowestCommonAncestor(root, p, q):
    path_p = []
    path_q = []
    preorder(root, p, path_p)
    preorder(root, q, path_q)
    path_p += [p]
    path_q += [q]
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i].val != path_q[i].val:
            break
    return path_p[i - 1]

def preorder(root, node, path):
    if not root:
        return False
    path += [root]
    if root.val == node.val:
        return True
    res1 = preorder(root.left, node, path)
    res2 = preorder(root.right, node, path)
    if res1 or res2:
        return True
    path.pop()
    return False

def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if not r:
        return l
    elif not l:
        return r
    else:
        return root
