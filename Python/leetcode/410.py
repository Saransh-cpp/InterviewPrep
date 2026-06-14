def splitArray(nums, k):
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = (low + high) >> 1
        curr_sum = 0
        s_arr = 1
        for i in range(len(nums)):
            if curr_sum + nums[i] > mid:
                s_arr += 1
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
        if s_arr > k:
            low = mid + 1
        else:
            high = mid - 1
    return low
