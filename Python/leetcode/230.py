cnt = 0
res = 0

def kthSmallest(root, k):
    inorder(root, k)
    return res

def inorder(root, k):
    if not root:
        return
    inorder(root.left, k)
    cnt += 1
    if k == cnt:
        res = root.val
        return
    inorder(root.right, k)


from collections import deque


def kthSmallest(root, k):
    st = deque()
    cnt = 0
    res = []

    while True:
        if cnt == k:
            break
        if root:
            st.append(root)
            root = root.left
        else:
            if not st:
                break
            el = st.pop()
            res += [el.val]
            cnt += 1
            root = el.right

    return res[-1]
