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
