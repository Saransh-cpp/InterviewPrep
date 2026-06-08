def findMin(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) >> 1
        left_sorted = nums[low] <= nums[mid]
        right_sorted = nums[mid] <= nums[high]
        if left_sorted and right_sorted:
            return nums[low]
        elif left_sorted:
            low = mid + 1
        else:
            high = mid
