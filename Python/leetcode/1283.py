from math import ceil


def smallestDivisor(nums, threshold):
    low = 1
    high = max(nums)
    while low <= high:
        mid = (low + high) >> 1
        sm = 0
        for num in nums:
            sm += ceil(num / mid)
        if sm <= threshold:
            high = mid - 1
        else:
            low = mid + 1
    return low
