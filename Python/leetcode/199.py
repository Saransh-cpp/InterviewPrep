from collections import deque


def rightSideView(root):
    if not root: return []

    res = []
    st = deque([root])
    while st:
        size = len(st)
        curr = []
        for i in range(size):
            el = st.popleft()
            curr += [el.val]
            if el.left: st.append(el.left)
            if el.right: st.append(el.right)
        res += [curr[-1]]
    return res
