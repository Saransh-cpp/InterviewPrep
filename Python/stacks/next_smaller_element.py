from collections import deque


def nextSmallerElements(arr):
    st = deque()
    res = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while st and st[-1] >= arr[i]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(arr[i])
    return res
