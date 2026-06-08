def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] == target:
            return True
        if nums[mid] == nums[low] and nums[mid] == nums[high]:
            high -= 1
            low += 1
            continue
        left_sorted = nums[low] <= nums[mid]
        if left_sorted:
            if nums[low] <= target and nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target and nums[high] >= target:
                low = mid + 1
            else:
                high = mid - 1
    return False
