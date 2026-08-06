def deleteNode(root, key):
    temp = root
    prev = None
    while True:
        if not temp:
            return root
        if temp.val == key:
            break
        elif temp.val < key:
            prev = temp
            temp = temp.right
        else:
            prev = temp
            temp = temp.left
    if temp == root:
        if not temp.left and not temp.right:
            return None
        elif not temp.left:
            return temp.right
        elif not temp.right:
            return temp.left
        else:
            right_subtree = temp.right
            root = temp.left
            prev = root
            while prev.right:
                prev = prev.right
            prev.right = right_subtree
    elif not temp.left and not temp.right:
        if prev.left == temp:
            prev.left = None
        else:
            prev.right = None
    elif not temp.left:
        if prev.left == temp:
            prev.left = temp.right
        else:
            prev.right = temp.right  
    elif not temp.right:
        if prev.left == temp:
            prev.left = temp.left
        else:
            prev.right = temp.left  
    else:
        right_subtree = temp.right
        if prev.left == temp:
            prev.left = temp.left
            prev = prev.left
        else:
            prev.right = temp.left  
            prev = prev.right
        while prev.right:
            prev = prev.right
        prev.right = right_subtree

    return root
