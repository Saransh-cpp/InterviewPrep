def maxSubArray(nums):
    max_summ = nums[0]
    summ = 0
    for num in nums:
        summ += num
        if summ > max_summ:
            max_summ = summ
        if summ < 0:
            summ = 0
    return max_summ
