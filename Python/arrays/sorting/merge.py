def mergeSort(nums):
    low = 0
    high = len(nums) - 1
    recurse(low, high, nums)
    return nums

def recurse(low, high, nums):
    if low >= high: return
    mid = (low + high) >> 1
    recurse(low, mid, nums)
    recurse(mid + 1, high, nums)
    merge(low, mid, high, nums)

def merge(low, mid, high, nums):
    i = low
    j = mid + 1
    merged = []
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            merged += [nums[i]]
            i += 1
        else:
            merged += [nums[j]]
            j += 1
    while i <= mid:
        merged += [nums[i]]
        i += 1
    while j <= high:
        merged += [nums[j]]
        j += 1
    for p in range(low, high + 1):
        nums[p] = merged[p - low]
