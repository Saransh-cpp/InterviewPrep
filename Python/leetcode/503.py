from collections import deque


def nextGreaterElements(nums):
    st = deque()
    res = []
    n = len(nums)
    for i in range(2 * n - 1, -1, -1):
        if len(st) == 0 or st[-1] > nums[i % n]:
            if i < n:
                res.append(st[-1])
        else:
            while len(st) > 0 and st[-1] <= nums[i % n]:
                st.pop()
            if i < n:
                if len(st) > 0:
                    res.append(st[-1])
                else:
                    res.append(-1)
        st.append(nums[i % n])
    return res[::-1]


def nextGreaterElements(nums):
    st = deque()
    n = len(nums)
    res = [-1] * n
    for i in range(2 * n - 1, -1, -1):
        el = nums[i % n]
        while st and st[-1] <= el:
            st.pop()
        if i < n and st:
                res[i] = st[-1]
        st.append(el)
    return res
