def rearrangeArray(nums):
    pos = 0
    neg = 1
    res = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            res[pos] = nums[i]
            pos += 2
        else:
            res[neg] = nums[i]
            neg += 2
    return res
