def singleNonDuplicate(nums):
    if len(nums) == 1: return nums[0]

    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) >> 1
        if mid == 0 or mid == len(nums) - 1:
            return nums[mid]
        elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif nums[mid] == nums[mid - 1]:
            if mid & 1:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if mid & 1:
                high = mid - 1
            else:
                low = mid + 1
