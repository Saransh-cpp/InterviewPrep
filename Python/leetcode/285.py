def succPredBST(root, key):
    ceil = float("inf")
    floor = -float("inf")

    temp = root
    while True:
        if not temp: break
        if temp.data < key:
            floor = max(floor, temp.data)
            temp = temp.right
        else:
            temp = temp.left

    temp = root
    while True:
        if not temp: break
        if temp.data > key:
            ceil = min(ceil, temp.data)
            temp = temp.left
        else:
            temp = temp.right

    if floor == -float("inf"):
        floor = -1
    if ceil == float("inf"):
        ceil = -1
    return [floor, ceil]
