def findPeakElement(nums):
    if len(nums) == 1: return 0

    low = 1
    high = len(nums) - 2
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return 0 if nums[1] < nums[0] else len(nums) - 1
