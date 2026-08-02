def quickSort(nums):
    recurse(nums, 0, len(nums) - 1)
    return nums

def recurse(nums, low, high):
    if low >= high: return
    i = low
    j = high
    pivot = nums[low]
    while i < j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    recurse(nums, low, j - 1)
    recurse(nums, j + 1, high)
