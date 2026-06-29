from collections import deque


def nextSmallerElement(nums):
    st = deque()
    n = len(nums)
    nse = [n] * n
    for i in range(n - 1, -1, -1):
        while st and nums[st[-1]] > nums[i]:
            st.pop()
        if st:
            nse[i] = st[-1]
        st.append(i)
    return nse

def prevSmallerElement(nums):
    st = deque()
    n = len(nums)
    pse = [-1] * n
    for i in range(n):
        while st and nums[st[-1]] >= nums[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse

def sumSubarrayMins(arr) :
    summ = 0
    pse = prevSmallerElement(arr)
    nse = nextSmallerElement(arr)
    for i in range(len(arr)):
        summ += arr[i] * (i - pse[i]) * (nse[i] - i)
    return int(summ % (1e9 + 7))
