from collections import deque


def removeKdigits(num, k):
    if k == len(num): return "0"

    st = deque()
    res = ""
    for i, n in enumerate(num):
        while st and st[-1] > n and k > 0:
            st.pop()
            k -= 1
        st.append(n)

    while k > 0:
        st.pop()
        k -= 1

    res = "".join(list(st)) + res
    res = res.lstrip("0")
    if res == num:
        res = res[:-k]

    return res if res else "0"
