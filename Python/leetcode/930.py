def numSubarraysWithSum(nums, goal):
    d = {0: 1}
    summ = 0
    count = 0
    for i in range(len(nums)):
        summ += nums[i]
        if summ - goal in d:
            count += d[summ - goal]
        d[summ] = d.get(summ, 0) + 1
    return count

def numSubarraysWithSum(nums, goal):
    return numSubarraysWithSumLTE(nums, goal) - numSubarraysWithSumLTE(nums, goal - 1)

def numSubarraysWithSumLTE(nums, goal):
    if goal < 0: return 0
    r = 0
    l = 0
    summ = 0
    count = 0
    while r < len(nums):
        summ += nums[r]
        while summ > goal:
            summ -= nums[l]
            l += 1
        count += (r - l + 1)
        r += 1
    return count
