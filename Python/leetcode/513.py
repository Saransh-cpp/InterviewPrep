from collections import deque


def findBottomLeftValue(root):
    res = 0
    st = deque([root])
    while st:
        curr = []
        size = len(st)
        for i in range(size):
            el = st.popleft()
            curr += [el.val]
            if el.left: st.append(el.left)
            if el.right: st.append(el.right)
        res = curr[0]
    return res
