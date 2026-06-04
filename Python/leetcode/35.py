def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    mid = high // 2
    while low <= high:
        if nums[mid] == target: return mid
        elif nums[mid] > target:
            high = mid - 1
            mid = (low + high) >> 1
        else:
            low = mid + 1
            mid = (low + high) >> 1
    if nums[mid] < target:
        return mid + 1
    if mid == -1: return 0
    return mid
