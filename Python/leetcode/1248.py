def numberOfSubarrays(nums, k):
    return numSubarraysWithSumLTE(nums, k) - numSubarraysWithSumLTE(nums, k - 1)

def numSubarraysWithSumLTE(nums, goal):
    if goal < 0: return 0
    r = 0
    l = 0
    summ = 0
    count = 0
    while r < len(nums):
        summ += nums[r] % 2
        while summ > goal:
            summ -= nums[l] % 2
            l += 1
        count += (r - l + 1)
        r += 1
    return count
