def searchRange(nums, target):
    low = 0
    high = len(nums) - 1
    mid = high // 2
    lowest = None
    while low <= high:
        if nums[mid] == target:
            lowest = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) >> 1

    low = 0
    high = len(nums) - 1
    mid = high // 2
    highest = None
    while low <= high:
        if nums[mid] == target:
            highest = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) >> 1

    if lowest is not None and highest is not None:
        return [lowest, highest]
    return [-1, -1]
