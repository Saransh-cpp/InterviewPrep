count = 0

def numberOfInversions(nums):
    recurse(nums, 0, len(nums) - 1)
    return count

def recurse(nums, low, high):
    if low >= high:
        return
    mid = (low + high) >> 1
    recurse(nums, low, mid)
    recurse(nums, mid + 1, high)
    merge(nums, low, mid, high)

def merge(nums, low, mid, high):
    i = low
    j = mid + 1
    merged = []
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            merged += [nums[i]]
            i += 1
        else:
            count += (mid - i + 1)
            merged += [nums[j]]
            j += 1
    while i <= mid:
        merged += [nums[i]]
        i += 1
    while j <= high:
        merged += [nums[j]]
        j += 1
    for i in range(low, high + 1):
        nums[i] = merged[i - low]
