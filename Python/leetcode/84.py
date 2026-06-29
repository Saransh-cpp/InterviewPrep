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
        while st and nums[st[-1]] >= nums[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse

def largestRectangleArea(heights):
    area = 0
    pse = prevSmallerElement(heights)
    nse = nextSmallerElement(heights)
    for i in range(len(heights)):
        area = max(area, heights[i] * (nse[i] - pse[i] - 1))
    return area
