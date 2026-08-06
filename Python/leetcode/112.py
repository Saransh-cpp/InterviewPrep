def hasPathSum(root, targetSum):
    if not root:
        return False
    targetSum -= root.val
    if not root.right and not root.left:
        return targetSum == 0
    lpath = hasPathSum(root.left, targetSum)
    rpath = hasPathSum(root.right, targetSum)
    return lpath or rpath
