from collections import deque


def nextSmallerElement(nums):
    st = deque()
    n = len(nums)
    nse = [n] * n
    for i in range(n - 1, -1, -1):
        while st and nums[st[-1]] >= nums[i]:
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
        while st and nums[st[-1]] > nums[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse

def nextGreaterElement(nums):
    st = deque()
    n = len(nums)
    nge = [n] * n
    for i in range(n - 1, -1, -1):
        while st and nums[st[-1]] < nums[i]:
            st.pop()
        if st:
            nge[i] = st[-1]
        st.append(i)
    return nge

def prevGreaterElement(nums):
    st = deque()
    n = len(nums)
    pge = [-1] * n
    for i in range(n):
        while st and nums[st[-1]] <= nums[i]:
            st.pop()
        if st:
            pge[i] = st[-1]
        st.append(i)
    return pge

def subArrayRanges(nums):
    nge = nextGreaterElement(nums)
    pge = prevGreaterElement(nums)
    pse = prevSmallerElement(nums)
    nse = nextSmallerElement(nums)

    small_sum = 0
    great_sum = 0
    for i in range(len(nums)):
        small_sum += nums[i] * (nse[i] - i) * (i - pse[i])
        great_sum += nums[i] * (nge[i] - i) * (i - pge[i])

    return great_sum - small_sum
