def subarraySum(nums, k):
    left = 0
    summ = 0
    for right in range(len(nums)):
        summ += nums[right]
        if summ > k:
            summ -= nums[left]
            left += 1
        elif summ == k:
            return summ
