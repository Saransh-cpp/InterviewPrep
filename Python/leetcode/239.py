from collections import deque


def maxSlidingWindow(nums, k):
    d = deque()
    count = 1
    res = []
    for i, num in enumerate(nums):
        if d and d[0] <= i - k:
            d.popleft()

        while d and nums[d[-1]] < num:
            d.pop()

        d.append(i)

        if count >= k:
            res.append(nums[d[0]])

        count += 1
    return res
