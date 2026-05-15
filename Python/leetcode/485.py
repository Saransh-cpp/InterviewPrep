def findMaxConsecutiveOnes(nums):
    maxn = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1: count += 1
        else:
            if count > maxn:
                maxn = count
            count = 0
    return maxn if maxn >= count else count
