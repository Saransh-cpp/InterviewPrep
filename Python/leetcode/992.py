def subarraysWithKDistinct(nums, k):
    return numSubarraysWithSumLTE(nums, k) - numSubarraysWithSumLTE(nums, k - 1)

def numSubarraysWithSumLTE(nums, goal):
    if goal < 0: return 0
    r = 0
    l = 0
    d = {}
    count = 0
    while r < len(nums):
        d[nums[r]] = d.get(nums[r], 0) + 1
        while len(d) > goal:
            d[nums[l]] -= 1
            if d[nums[l]] == 0:
                del d[nums[l]]
            l += 1
        count += (r - l + 1)
        r += 1
    return count
